from ninja import Router

router = Router()

# Register v2 routers
# ---
from .account.router import router as account_router  # noqa: E402

router.add_router("/account/", account_router, tags=["v2/Account"])

# ---
from .payment.router import router as payment_router  # noqa: E402

router.add_router("/payment/", payment_router, tags=["v2/Payment"])
