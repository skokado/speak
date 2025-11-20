from ninja import Router

from my_proj.settings.payment import settings

router = Router()


@router.get("/")
async def payment_root(request):
    print(f"DEBUG: {settings.stripe_api_key=},{settings.stripe_webhook_secret=}")
    return {"message": "it works."}
