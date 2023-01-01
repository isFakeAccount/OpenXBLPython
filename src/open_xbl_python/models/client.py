import asyncio

from .xbox_account import XBOXAccount
from ..utils.endpoints import API_PATH
from ..utils.misc import create_logger


class Client(XBOXAccount):
    def __init__(self, api_key: str, proxy: str, language: str):
        super(Client, self).__init__(api_key=api_key, proxy=proxy, language=language)
        account_info = asyncio.run(self.account())
        self.logger = create_logger(module_name=__name__)
        for result in account_info.get("profileUsers")[0].get("settings"):
            if result.get("id") == "Gamertag":
                self.logger.info(f"Logged in as {result.get('value')}")
                break

    @property
    async def gamertag(self):
        pass

    @property
    async def xuid(self):
        pass

    @property
    async def friends(self):
        pass

    async def presence(self):
        pass

    async def conversations(self):
        pass

    async def achievements(self):
        pass

    async def game_achievements(self):
        pass

    async def account(self):
        return await self.request_builder.get(endpoint=API_PATH["account"])
