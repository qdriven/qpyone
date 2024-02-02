from fastapi import APIRouter

from qpyone.app.echo.schemas import EchoResponse

echo_router = APIRouter(prefix="/echo",
                        tags=["echo"],
                        responses={404: {"description": "Not found"}})


@echo_router.get("/")
async def echo():
    return EchoResponse(msg="Pong!")
