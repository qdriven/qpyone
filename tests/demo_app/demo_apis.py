
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()
static_file_abspath = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_file_abspath), name="static")


@app.get("/demo/json",status_code=200)
def demo():
    return {"message": "Hello World"}

@app.get("/demo/static")
def index_html():
    return FileResponse(f"{static_file_abspath}/index.html")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
