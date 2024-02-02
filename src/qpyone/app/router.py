from fastapi import APIRouter

from qpyone.app.echo.endpoints import echo_router

app_router = APIRouter(prefix="/api")

app_router.include_router(echo_router)
