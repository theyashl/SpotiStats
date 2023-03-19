import json
from utils.common import CacheUtils, AuthUtils


class Auth:
    """This class will handle the authentication of spotify user
    """
    def on_get(self, req: object, resp: object) -> None:
        """Handles callback request to get sign in to application
        This method will create a auth session with Spotify to handler further requests

        :param req: Request object of falcon containing request related data
        :type req: object
        :param resp: Response object of falcon containing response related data
        :type resp: object
        """
        _ = resp
        auth_manager = AuthUtils.get_auth_manager()
        auth_manager.get_access_token(req)

    def on_get_sign_out(self, req: object, resp: object) -> None:
        """Handler GET request to get sign out of application

        :param req: Request object of falcon containing request related data
        :type req: object
        :param resp: Response object of falcon containing response related data
        :type resp: object
        """
        _, _ = req, resp
        CacheUtils.delete_cache()
        response = {
            "message": "OK"
        }
        resp.text = json.dumps(response)
