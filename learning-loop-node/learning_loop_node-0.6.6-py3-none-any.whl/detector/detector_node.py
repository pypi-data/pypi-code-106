from . import operation_mode
from .operation_mode import OperationMode
from .detector import Detector
from .rest import detect, upload
from ..rest import downloads
from ..node import Node
from ..status import State
from ..status import DetectionStatus, State
from ..context import Context
from fastapi.encoders import jsonable_encoder
from fastapi_utils.tasks import repeat_every
from typing import List, Optional, Union
import shutil
import os
import contextlib
import logging
from learning_loop_node.globals import GLOBALS
import subprocess
import asyncio
import numpy as np
from fastapi_socketio import SocketManager
from . import Detections
from . import Outbox
from threading import Thread


class DetectorNode(Node):
    update_frequency = 10

    def __init__(self, name: str, detector: Detector, uuid: str = None):
        super().__init__(name, uuid)
        self.detector = detector
        self.organization = os.environ.get('LOOP_ORGANIZATION', None) or os.environ.get('ORGANIZATION', None)
        self.project = os.environ.get('LOOP_PROJECT', None) or os.environ.get('PROJECT', None)
        assert self.organization, 'Detector node needs an organization'
        assert self.project, 'Detector node needs an project'
        self.operation_mode = OperationMode.Startup
        self.connected_clients = []
        self.outbox = Outbox()
        self.target_model = None
        self.include_router(detect.router, tags=["detect"])
        self.include_router(upload.router, prefix="")
        self.include_router(operation_mode.router, tags=["operation_mode"])

        @self.on_event("startup")
        @repeat_every(seconds=self.update_frequency, raise_exceptions=False, wait_first=False)
        async def _check_for_update() -> None:
            await self.check_for_update()

        @self.on_event("startup")
        async def _load_model() -> None:
            self.detector.load_model()
            self.operation_mode = OperationMode.Check_for_updates

        @self.on_event("startup")
        @repeat_every(seconds=30, raise_exceptions=False, wait_first=False)
        def submit() -> None:
            thread = Thread(target=self.outbox.upload)
            thread.start()

        sio = SocketManager(app=self)

        @self.sio.on("detect")
        async def _detect(sid, data) -> None:
            try:
                np_image = np.frombuffer(data['image'], np.uint8)
                return await self.get_detections(np_image, data.get('mac', None), data.get('tags', []), data.get('active_learning', True))
            except Exception as e:
                logging.exception('could not detect via socketio')
                with open('/tmp/bad_img_from_socket_io.jpg', 'wb') as f:
                    f.write(data['image'])
                return {'error': str(e)}

        @self.sio.on("info")
        async def _info(sid) -> None:
            if self.detector.current_model:
                return self.detector.current_model.__dict__
            return 'No model loaded'

        @self.sio.on('upload')
        async def _upload(sid, data):
            loop = asyncio.get_event_loop()
            try:
                await loop.run_in_executor(None, lambda: self.outbox.save(data['image'], Detections(), ['picked_by_system']))
            except Exception as e:
                logging.exception('could not upload via socketio')
                return {'error': str(e)}

        @self.sio.event
        def connect(sid, environ, auth):
            self.connected_clients.append(sid)

        @self.on_event("shutdown")
        async def shutdown():
            for sid in self.connected_clients:
                await self.sio.disconnect(sid)

    async def check_for_update(self):
        if self.operation_mode == OperationMode.Startup:
            return
        try:
            logging.info(f'periodically checking operation mode. Current mode is {self.operation_mode}')
            update_to_model_id = await self.send_status()
            if self.detector.current_model:
                logging.info(
                    f'Current model: {self.detector.current_model.version} with id {self.detector.current_model.id}')
            else:
                logging.info(f'no model loaded')
            if self.operation_mode != OperationMode.Check_for_updates:
                logging.info(f'not checking for updates; operation mode is {self.operation_mode}')
                return
            if self.target_model is None:
                logging.info(f'not checking for updates; no target model selected')
                return
            logging.info('going to check for new updates')
            if not self.detector.current_model or self.target_model != self.detector.current_model.version:
                logging.info(
                    f'Current model "{self.detector.current_model.version if self.detector.current_model else "-"}" needs to be updated to {self.target_model}')
                with pushd(GLOBALS.data_folder):
                    model_symlink = 'model'
                    target_model_folder = f'models/{self.target_model}'
                    shutil.rmtree(target_model_folder, ignore_errors=True)
                    os.makedirs(target_model_folder)
                    try:
                        await downloads.download_model(
                            target_model_folder,
                            Context(organization=self.organization, project=self.project),
                            update_to_model_id,
                            self.detector.model_format
                        )
                        try:
                            os.unlink(model_symlink)
                            os.remove(model_symlink)
                        except:
                            pass
                        os.symlink(target_model_folder, model_symlink)
                        logging.info(f'Updated symlink for model to {os.readlink(model_symlink)}')
                        self.reload(because='new model installed')
                    except downloads.DownloadError as e:
                        self.status.latest_error = f'download failed: {e.cause}'
            else:
                logging.info('Versions are identic. Nothing to do.')
        except Exception:
            logging.exception(f'check_for_update failed')
            self.status.latest_error = 'could not check for model update'

    async def send_status(self) -> Union[str, bool]:
        if not self.sio_client.connected:
            logging.error('could not send status -- we are not connected to the Learning Loop')
            return False
        status = DetectionStatus(
            id=self.uuid,
            name=self.name,
            state=self.status.state,
            operation_mode=self.operation_mode,
            current_model=self.detector.current_model.version if self.detector.current_model else None,
            target_model=self.target_model,
            latest_error=self.status.latest_error,
            model_format=self.detector.model_format,
        )
        logging.debug(f'sending status {status}')
        response = await self.sio_client.call('update_detector', (self.organization, self.project, jsonable_encoder(status)), timeout=1)
        try:
            self.target_model = response['payload']['target_model_version']
            logging.debug(f'After sending status. Target_model is {self.target_model}')
            return response['payload']['target_model_id']
        except:
            logging.error('Could not send status to loop')
            return False

    def get_state(self):
        return State.Online

    async def set_operation_mode(self, mode: OperationMode):
        self.operation_mode = mode
        await self.send_status()

    def reload(self, because: str):
        '''provide a cause for the reload'''

        print('########## reloading app because ' + because, flush=True)
        if os.path.isfile('/app/restart/restart.py'):
            subprocess.call(['touch', '/app/restart/restart.py'])
        else:
            subprocess.call(['touch', '/app/main.py'])

    async def get_detections(self, raw_image, mac: str, tags: str, active_learning=True):
        loop = asyncio.get_event_loop()
        # image = await loop.run_in_executor(None, lambda: cv2.imdecode(np_image, cv2.IMREAD_COLOR))
        detections = await loop.run_in_executor(None, self.detector.evaluate, raw_image)
        info = "\n    ".join([str(d) for d in detections.box_detections])
        logging.info(f'detected:\n    {info}')
        # if active_learning:
        #     thread = Thread(target=learn, args=(detections, mac, tags, image))
        #     thread.start()
        return jsonable_encoder(detections)

    async def upload_images(self, images: List[bytes]):
        loop = asyncio.get_event_loop()
        for image in images:
            await loop.run_in_executor(None, lambda: self.outbox.save(image, Detections(), ['picked_by_system']))


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)
