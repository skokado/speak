from typing import Literal
from ninja import Router, Schema

router = Router()


class AccountV2RootResponse(Schema):
    message: Literal["it works v2!"]


@router.get("/", response=AccountV2RootResponse)
def account_v2_root(request):
    return {"message": "it works v2!"}
