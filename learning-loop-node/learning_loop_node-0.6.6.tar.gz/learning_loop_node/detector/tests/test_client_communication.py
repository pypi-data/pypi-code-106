import pytest
from learning_loop_node import DetectorNode
import requests
import json
import os
from glob import glob


def test_rest_detect(test_detector_node: DetectorNode):
    image = {('file', open('detector/tests/test.jpg', 'rb'))}
    headers = {'mac': '0:0:0:0', 'tags':  'some_tag'}
    request = requests.post(f'http://localhost:{pytest.detector_port}/detect', files=image, headers=headers)
    assert request.status_code == 200

    json_content = json.loads(request.content.decode('utf-8'))
    assert len(json_content['box_detections']) == 1
    assert json_content['box_detections'][0]['category_name'] == 'some_category_name'


@pytest.mark.asyncio
async def test_sio_detect(test_detector_node: DetectorNode, sio_client):
    with open('detector/tests/test.jpg', 'rb') as f:
        image_bytes = f.read()
    result = await sio_client.call('detect', {'image': image_bytes})
    assert len(result['box_detections']) == 1
    assert result['box_detections'][0]['category_name'] == 'some_category_name'


def test_rest_detect(test_detector_node: DetectorNode):
    image = {('file', open('detector/tests/test.jpg', 'rb'))}
    headers = {'mac': '0:0:0:0', 'tags':  'some_tag'}
    response = requests.post(f'http://localhost:{pytest.detector_port}/detect', files=image, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert len(result['box_detections']) == 1
    assert result['box_detections'][0]['category_name'] == 'some_category_name'


def test_rest_upload(test_detector_node: DetectorNode):
    assert test_detector_node.outbox.path.startswith('/tmp')

    def get_outbox_files():
        files = glob(f'{test_detector_node.outbox.path}/**/*', recursive=True)
        return [file for file in files if os.path.isfile(file)]

    assert len(get_outbox_files()) == 0
    image = {('files', open('detector/tests/test.jpg', 'rb'))}
    response = requests.post(f'http://localhost:{pytest.detector_port}/upload', files=image)
    assert response.status_code == 200
    assert len(get_outbox_files()) == 2, 'There should be one image and one .json file.'


@pytest.mark.asyncio
async def test_sio_upload(test_detector_node: DetectorNode, sio_client):
    assert test_detector_node.outbox.path.startswith('/tmp')

    def get_outbox_files():
        files = glob(f'{test_detector_node.outbox.path}/**/*', recursive=True)
        return [file for file in files if os.path.isfile(file)]

    assert len(get_outbox_files()) == 0

    with open('detector/tests/test.jpg', 'rb') as f:
        image_bytes = f.read()
    result = await sio_client.call('upload', {'image': image_bytes})
    assert result == None

    assert len(get_outbox_files()) == 2, 'There should be one image and one .json file.'
