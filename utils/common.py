import json
from spotipy.cache_handler import MemoryCacheHandler
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify


class CacheUtils:
    """This class will hold common utility attributes/methods
    required by an application
    """
    @classmethod
    def __init__(cls):
        """Constructor for Utils class which will instantiate Memory Cache Handler
        """
        cls.__cache_handler = MemoryCacheHandler()

    @classmethod
    def get_cache(cls) -> object:
        """This method is responsible for exposing cache_handler object

        :return: returns the centralised object of cache_handler
        :rtype: object
        """
        try:
            cache_handler = cls.__cache_handler
        except AttributeError:
            cls.__init__()
            cache_handler = cls.__cache_handler
        return cache_handler
    
    @classmethod
    def delete_cache(cls) -> None:
        """This method will delete the instance of cache handler
        """
        try:
            del cls.__cache_handler
        except AttributeError:
            # already logged out
            pass


class AuthUtils:
    """Class to handler the auth manager object for Spotipy
    """
    @classmethod
    def __init__(cls):
        """Constructor for Auth Utils. Will initialize auth manager object
        """
        secrets = cls.__read_secrets()
        cls.__auth_manager = SpotifyOAuth(
            client_id=secrets["client_id"],
            client_secret=secrets["client_secret"],
            redirect_uri=secrets["redirect_uri"],
            scope=secrets["scope"],
            cache_handler=CacheUtils.get_cache()
        )

    @classmethod
    def __read_secrets(cls) -> dict:
        with open("secrets.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @classmethod
    def get_auth_manager(cls) -> object:
        """this method will provide access to auth manager object

        :return: auth manager object
        :rtype: object
        """
        try:
            auth_manager = cls.__auth_manager
        except AttributeError:
            cls.__init__()
            auth_manager = cls.__auth_manager
        return auth_manager


class AppUtils:
    """Utility class for handling Spotipy's Spotify app instance
    """
    @classmethod
    def __init__(cls):
        cls.__sp = Spotify(auth_manager=AuthUtils.get_auth_manager())

    @classmethod
    def get_spotify(cls) -> object:
        """expose spotipy's spotify app to resources

        :return: object of spotipy's spotify
        :rtype: object
        """
        try:
            spotify_app = cls.__sp
        except AttributeError:
            cls.__init__()
            spotify_app = cls.__sp
        return spotify_app
