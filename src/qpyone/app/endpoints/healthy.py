
from fastapi import APIRouter
from qpyone.app.models.responses import AppReadyResponse, ErrorResponse
import logging

router = APIRouter()
log = logging.getLogger(__name__)

@router.get("/healthy",tags =["health"],
summary="Check Environment is Ready",
status_code=200,
responses = {502: {"model":ErrorResponse}},
response_model=AppReadyResponse
)
async def readiness_check() -> AppReadyResponse:
     """Run basic application health check.

    If the application is up and running then this endpoint will return simple
    response with status ok. Moreover, if it has Redis enabled then connection
    to it will be tested. If Redis ping fails, then this endpoint will return
    502 HTTP error.
    \f

    Returns:
        response (ReadyResponse): ReadyResponse model object instance.

    Raises:
        HTTPException: If applications has enabled Redis and can not connect
            to it. NOTE! This is the custom exception, not to be mistaken with
            FastAPI.HTTPException class.

    """
    log.info("Checking application health...,/healthy")
    if not await RedisClient.ping():
        log.error("Redis is not ready!")
        raise HTTPException(status_code=502, detail="Redis is not ready!"
