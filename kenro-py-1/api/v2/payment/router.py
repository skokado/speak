from ninja import Router

router = Router()


@router.get("/")
def payment_v2_root():
    return {"message": "it works v2!"}
