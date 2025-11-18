from typing import Literal
from ninja import Router, Schema

from my_proj.settings.account import settings

router = Router()


class RootResponse(Schema):
    message: Literal["it works."]


@router.get("/", response=RootResponse)
async def account_root(request):
    print(f"DEBUG: {settings.cognito_app_client_id=},{settings.cognito_user_pool_id=}")
    return {"message": "it works."}
