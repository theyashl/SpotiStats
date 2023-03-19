import json
from utils.common import AppUtils


class User:
    """Handle the User resource.
    """
    def on_get(self, req: object, resp: object) -> None:
        """Handle the GET request. Serves current user information

        :param req: request object of Falcon
        :type req: object
        :param resp: response object of Falcon
        :type resp: object
        """
        _ = req
        app = AppUtils.get_spotify()
        user = app.me()
        resp.text = json.dumps(user)

    def on_get_top_tracks(self, req: object, resp: object) -> None:
        """Handles the GET request for User's Top Tracks

        :param req: request object of Falcon
        :type req: object
        :param resp: response object of Falcon
        :type resp: object
        """
        # time range, one of: ['short_term', 'medium_term', 'long_term']
        time_range = req.get_param("range", "short_term") # defaults to: short_term
        # result limit between 0 to 50
        limit = req.get_param("limit", 20) # defaults to 20
        app = AppUtils.get_spotify()
        top_tracks = app.current_user_top_tracks(time_range=time_range, limit=limit)
        resp.text = json.dumps(top_tracks)
