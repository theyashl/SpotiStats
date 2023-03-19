import falcon

from resources.auth import Auth
from resources.user import User
from utils.common import CacheUtils, AuthUtils, AppUtils


# instantiate utils
CacheUtils()
AuthUtils()
AppUtils()

app = falcon.App()
app.add_route('/auth', Auth())
app.add_route('/callback', Auth())
app.add_route('/sign_out', Auth(), suffix='sign_out')
app.add_route('/me', User())
app.add_route('/top_tracks', User(), suffix='top_tracks')
