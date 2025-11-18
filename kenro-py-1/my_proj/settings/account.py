from dataclasses import dataclass
import os
from typing import TYPE_CHECKING

from django.conf import settings

if TYPE_CHECKING:
    from my_proj.settings.types import AppEnv


app_env: "AppEnv" = settings.APP_ENV


@dataclass(frozen=True)
class AccountSettings:
    cognito_user_pool_id: str
    cognito_app_client_id: str
    # ...


settings = AccountSettings(
    cognito_user_pool_id=f"{app_env}_dummy_pool_id",
    cognito_app_client_id=os.getenv("COGNITO_APP_CLIENT_ID", "dummy"),
    # ...
)
