import json
from contextlib import asynccontextmanager

import aiohttp
from dompower import DompowerClient

from dominsights.config import settings


class NotLoggedInError(RuntimeError):
    def __init__(self):
        super().__init__("Run `dominsights login` first.")


@asynccontextmanager
async def get_client():
    tokens = json.loads(settings.token_file.read_text())

    async with aiohttp.ClientSession() as session:

        def token_callback(access, refresh):
            settings.token_file.write_text(json.dumps({"access_token": access, "refresh_token": refresh}))

        client = DompowerClient(
            session,
            access_token=tokens["access_token"],
            refresh_token=tokens["refresh_token"],
            token_update_callback=token_callback,
        )

        yield client
