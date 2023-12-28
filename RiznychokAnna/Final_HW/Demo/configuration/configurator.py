import configparser
import os

filename = os.path.dirname(__file__) + '/config.ini'


class Config:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(filename)

    def get_bot_token(self):
        return self._config['Tokens']['bot']

    def get_api_token(self):
        return self._config['Tokens']['api']

    def get_api_url(self) -> str:
        return self._config['Url']['api_url']

    def get_movie_url(self) -> str:
        return self._config['Url']['movie_url']
