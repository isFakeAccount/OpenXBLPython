from .models.client import Client
from .models.open_xbl_base import OpenXBLBase


class OpenXBL(OpenXBLBase):
    """The OpenXBL class provides gateway access to Open XBL API.

    Instances of this class allows you to access the Open XBL API through convenient methods. To instantiate this class, see the following example:

    .. code-block:: python

        from open_xbl_python import OpenXBL

        xbl = OpenXBL(api_key=API_KEY)

    You make add proxy by passing argument `proxy="http://user:pass@some.proxy.com"`.

    """

    def __init__(self, api_key: str, proxy: str = "", language="en-US"):
        """Initialize a :class:`.OpenXBL` instance.

        :param api_key: The api key obtained from https://xbl.io/.
        :param proxy: Proxy URL for connected to API via proxy. (default: "")
        :param language: Language setting for the API. (default: en-US)

        To get the api key, please follow the guide on https://xbl.io/getting-started.

        """
        super().__init__(api_key=api_key, proxy=proxy, language=language)

    def client(self):
        """:returns: None"""
        return Client(api_key=self.api_key, proxy=self.proxy, language=self.language)
