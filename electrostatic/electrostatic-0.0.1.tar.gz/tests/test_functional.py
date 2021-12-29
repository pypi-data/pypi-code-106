"""Fynctional tests for electrostatic

These tests are for "functional" testing of the package.
These are not really unit tests, they are more along the lines of tests of the
behaviour of the package when being used the way we expect it to be used.

These serve as excellent smoke tests to verify that nothing is fundamentally broken.
"""
from pathlib import Path

import pytest
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_electrostatic_asgi_with_file_finder(request):
    """Test electrostatic ASGI can serve files with a single FileFinder on the default prefix"""

    rootdir = Path(request.config.rootdir)

    from electrostatic.asgi import Electrostatic
    from electrostatic.assets import FileAssetFinder

    file_dir = rootdir / "tests/sample/static1"
    app = Electrostatic(finder=FileAssetFinder([file_dir]))

    async with TestClient(app) as client:
        resp = await client.get("/hello.txt")
        assert resp.status_code == 200
        assert resp.text.strip() == "this is a plain text file"
        assert resp.headers.get("content-type") == 'text/plain; charset="utf-8"'

        resp = await client.get("/doesnotexist.txt")
        assert resp.status_code == 404
        assert resp.text.strip() == "Page not found"


# - Test with a wrapped application, make sure requests are passed through
# - Test with multiple Finders on different prefixes
# - Test with different mime types
# - Test with a very large file
# - Test with non-GET requests (method not allowed)
# - Test outside of prefixes (internal server error, probably)
# - Test with non-existent directory for FileFinder
