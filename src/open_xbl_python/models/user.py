from .xbox_account import XBOXAccount


class User(XBOXAccount):
    def __init__(self, api_key: str, proxy: str, language: str):
        super(User, self).__init__(api_key=api_key, proxy=proxy, language=language)

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
