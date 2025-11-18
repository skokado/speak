from dataclasses import dataclass
import os


@dataclass(frozen=True)
class PaymentSettings:
    stripe_api_key: str
    stripe_webhook_secret: str
    # ...


settings = PaymentSettings(
    stripe_api_key=os.getenv("STRIPE_API_KEY", "dummy"),
    stripe_webhook_secret=os.getenv("STRIPE_WEBHOOK_SECRET", "dummy"),
)
