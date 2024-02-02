import os

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
import uvicorn

from qpyone.app.router import app_router
from qpyone.constants import BASE_DIR


def create_app():
    app = FastAPI()
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(BASE_DIR, "static")),
        name="static",
    )

    app.include_router(app_router)
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0",
                port=9090, reload=True)
