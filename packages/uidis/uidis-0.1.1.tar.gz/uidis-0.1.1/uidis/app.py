from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

from .example_nav import Apps
from .lookups import Lookups
from .shared import DIR_ASSETS, HEADERS, __version__, pack

app = FastAPI()


@app.get("/.ui/version")
async def version():
    return pack(__version__)


@app.get("/.ui/navigation")
async def navigation():
    return pack(Apps)


@app.get("/.ui/lookup/{name}/{code}")
def lookup(name: str, code: str):
    try:
        return pack(Lookups[name][int(code)])
    except KeyError:
        return Response(status_code=404)


@app.get("/")
async def index():
    return FileResponse(DIR_ASSETS / "index.html", headers=HEADERS)


@app.get("/index.js")
async def index_js():
    return FileResponse(DIR_ASSETS / "index.js", headers=HEADERS)


@app.get("/index.css")
async def index_css():
    return FileResponse(DIR_ASSETS / "index.css", headers=HEADERS)
