import requests
import logging

from configuration.configurator import Config
from utils.utils import setup_logs

setup_logs()


class MovieRequests:
    def __init__(self):
        config = Config()
        self.movie_url = config.get_movie_url()
        self.headers = {
            "X-RapidAPI-Key": config.get_api_token(),
            "X-RapidAPI-Host": config.get_api_url()
        }

    def get_movies(self, title: str):
        querystring = {"s": title, "r": "json", "page": "1"}
        response = requests.get(self.movie_url, headers=self.headers, params=querystring)
        if 'False' not in response.text:
            logging.debug(f"[LIST_OF_MOVIES]: List of movies response has been got successfully. Url: {self.movie_url}")
            return response
        else:
            raise Exception(f"List of movies request error. Url: {self.movie_url}. Status: {response.text}.")

    def get_movie(self, id_film: str):
        querystring = {"r": "json", "i": id_film}
        response = requests.get(self.movie_url, headers=self.headers, params=querystring)
        if 'False' not in response.text:
            logging.debug(
                f"[MOVIE]: Movie response has been got successfully. Url: {self.movie_url}")
            return response
        else:
            raise Exception(f"Movie request error. Url: {self.movie_url}. Status: {response.text}.")
