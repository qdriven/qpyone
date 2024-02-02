import json

from fastapi import APIRouter, Response

gpt_router = APIRouter(prefix="/gpt")


@gpt_router.get("/")
async def api_info():
    return Response(content=json.dumps({"info": "QPyOne GPT API"}, indent=4),
                    media_type="application/json")
