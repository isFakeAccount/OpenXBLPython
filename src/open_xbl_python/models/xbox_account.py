from abc import ABC, abstractmethod

from .open_xbl_base import OpenXBLBase


class XBOXAccount(ABC, OpenXBLBase):
    def __init__(self, api_key: str, proxy: str, language: str):
        super(XBOXAccount, self).__init__(api_key=api_key, proxy=proxy, language=language)

    @property
    @abstractmethod
    async def gamertag(self):
        raise NotImplementedError

    @property
    @abstractmethod
    async def xuid(self):
        raise NotImplementedError

    @property
    @abstractmethod
    async def friends(self):
        raise NotImplementedError

    @abstractmethod
    async def presence(self):
        raise NotImplementedError

    @abstractmethod
    async def conversations(self):
        raise NotImplementedError

    @abstractmethod
    async def achievements(self):
        raise NotImplementedError

    @abstractmethod
    async def game_achievements(self):
        raise NotImplementedError
