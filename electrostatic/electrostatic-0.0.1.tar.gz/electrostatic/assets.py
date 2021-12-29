"""Asset handling for Electrostatic

Common asset handling code for both ASGI and WSGI implementations of Electrostatic.
Most of the code is sync, where necessary there is an async version of function calls
that it makes sense for, but to be honest, most of the code is fast enough that it does
not need or benefit from async.
"""
from io import BytesIO
from pathlib import Path
from threading import Thread
from typing import BinaryIO, Callable, Dict, Iterable, List, Optional, Tuple, Union

from .utils import get_mime_type


class BaseAsset(object):
    """Base class for asset handling"""

    status: int
    headers: List[Tuple[bytes, bytes]]
    _body: Optional[BytesIO] = None

    @property
    def fd(self) -> Optional[BinaryIO]:
        return None

    def body(self, *, chunk_size=4096, start=0, end=None) -> Iterable[bytes]:
        # If there is a file descriptor, use that; if not, use _body
        # If both are None, return b""
        if self.fd is not None:
            F = self.fd
            F.seek(start)
            while True:
                data = F.read(chunk_size)
                if not data:
                    return
                yield data
        elif self._body is not None:
            while True:
                data = self._body.read(chunk_size)
                if not data:
                    return
                yield data
        else:
            yield b""

    def __init__(
        self,
        *,
        status: int = 200,
        headers: Optional[List[Tuple[bytes, bytes]]] = None,
        body: Optional[bytes] = None,
    ):
        self.status = status
        self.headers = headers if headers is not None else []
        if body is not None:
            self._body = BytesIO(body)


class FileAsset(BaseAsset):
    """A regular static file asset, referencing a file stored on a filesystem"""

    _file_path: Path

    @property
    def fd(self) -> BinaryIO:
        return self._file_path.open("rb")

    def __init__(self, *, file_path: Path, **kwargs):
        super().__init__(**kwargs)
        self._file_path = file_path
        self.set_mime_headers()

    def set_mime_headers(self):
        mime_type = get_mime_type(self._file_path)
        if mime_type.startswith("text/"):
            self.headers.append(
                (b"Content-Type", f'{mime_type}; charset="utf-8"'.encode("utf-8"))
            )
        else:
            self.headers.append((b"Content-Type", mime_type.encode("utf-8")))


class BaseAssetFinder(object):
    """Asset Finder

    The base asset finder, used by both ASGI and WSGI applications to look up assets by
    url path.

    The base AssetFinder just returns a 404 not found asset for all paths.
    """

    # A cache of url paths to assets
    assets: Dict[str, BaseAsset]

    def __init__(self, **kwargs):
        self.assets = {}

    def __call__(self, path: str, prefix: Optional[str] = None) -> Optional[BaseAsset]:
        """Get an Asset for a particular path, or if it doesn't exist, either a 404 or None"""

        # Look up in the asset cache, and return it if it exists
        asset = self.assets.get(path, None)
        if asset:
            return asset
        return None

    def load_assets(self) -> None:
        """Load assets into cache. Note this can be called more than once e.g. to reload cache contents"""

        pass

    def startup(self) -> None:
        """Set up the asset cache, and do any other initialization for the Finder"""

        self.load_assets()


class FileAssetFinder(BaseAssetFinder):
    """An asset finder using the host filesystem"""

    # A map of url prefixes and the paths to search for assets
    paths: List[Path]
    # Serve index.html files (if False, just 404 for index URLs)
    serve_index: bool

    def __init__(self, paths: Iterable[Path], *, serve_index: bool = False, **kwargs):
        self.serve_index = serve_index
        self.paths = [path.resolve() for path in paths]

        super().__init__(**kwargs)

    def load_assets(self) -> None:
        """Iterate through our paths and set up the assets cache"""

        super().load_assets()

        def scan_path(root: Path, dir_path: Path) -> None:
            """Internal function called recursively"""
            if self.serve_index:
                if root == dir_path:
                    url = f"/"
                else:
                    url = f"{dir_path.relative_to(root)}"
                index_path = dir_path / "index.html"

                if url not in self.assets and index_path.exists():
                    self.assets[url] = FileAsset(file_path=index_path)

            for file_path in dir_path.iterdir():
                if file_path.is_dir():
                    # Recurse in
                    scan_path(root, file_path)
                elif file_path.exists():
                    url = f"/{file_path.relative_to(root)}"
                    if url not in self.assets and file_path.exists():
                        self.assets[url] = FileAsset(file_path=file_path)
                else:
                    # Not a directory and doesn't exist...could be permissions?
                    # Ignore for now, but maybe it should log a warning.
                    pass

        # We scan the prefix paths from longest to shortest (a more specific prefix should match "better")
        # Scan paths in order they were added for a particular prefix
        for path in self.paths:
            if not path.exists():
                # Missing file or directory...raise an error (or should we accept it silently?)
                raise RuntimeError(f"Static file path '{path}' is not a directory.")
            else:
                # Start a recursive scan into the path
                scan_path(path, path)


class WatchedFileAssetFinder(FileAssetFinder):
    """A special FileAssetFinder that monitors for changes to the filesystem

    This Finder monitors for filesystem updates, and reloads the cached assets accordingly.
    """

    watch_thread: Optional[Thread]

    def watch_for_changes(self):
        """Use watchdog to monitor for changes, and launch startup() again to load changes"""

        try:
            from watchdog.events import FileSystemEvent, FileSystemEventHandler
            from watchdog.observers import Observer
        except ImportError:
            raise RuntimeError(
                "Watchdog package not installed - install electrostatic with the 'watchdog' extra."
            )

        class PathEventHandler(FileSystemEventHandler):
            def __init__(self, event_callback: Callable[[FileSystemEvent], None]):
                self.event_callback = event_callback
                super().__init__()

            def on_any_event(self, event: FileSystemEvent) -> None:
                return self.event_callback(event)

        def reload(event: FileSystemEvent):
            # Note: this should really have a lock when it reloads; but since this is intended for dev only,
            #  maybe it doesn't matter.
            # Invalidate the asset cache
            self.assets = {}
            self.load_assets()

        watchdog_handler = PathEventHandler(reload)
        observer = Observer()
        for path in self.paths:
            observer.schedule(watchdog_handler, str(path), recursive=True)
        observer.start()
        observer.join()

    def startup(self) -> None:
        super().startup()
        # launch a thread that will monitor for changes, and trigger a reload of the assets if required
        self.watch_thread = Thread(
            name="watchdog-thread", target=self.watch_for_changes, daemon=True
        )
        self.watch_thread.start()
