import logging

from movie_requests import MovieRequests
from RiznychokAnna.Demo.utils.utils import format_str, setup_logs
from RiznychokAnna.Demo.utils.constants import Emojis

setup_logs()

# TODO:
#  1. Add logs (file, console)
#  2. Add docstrings
#  3. Handle exceptions
#  4. Handle missing keys in response json
#  5. Add emojis DONE
#  6. Add constants module DONE
#  7. Hide tokens (bot, api) DONE
#  8. Change logs format, colour (optional)
#  9. Host script on server
#  10. Reformat output message (optional)


class MovieInfo:
    def __init__(self):
        self._mr = MovieRequests()
        self._m_list = []
        self._m_dict = {}

    def get_movies_list(self):
        return self._m_list

    def _get_movies_id_dict(self, title: str):
        if self._m_dict:
            self._m_dict.clear()
        try:
            response = self._mr.get_movies(title)

            for movi in response.json()['Search']:
                self._m_dict[movi['Title']] = movi['imdbID']

            logging.debug(f"[MOVIE_INFO] Movies id dictionary was successfully created")
        except Exception as msg:
            logging.warning(f"OOPS, couldn't find desired movies. Error: {msg}")

    def create_movie_titles_list(self, title: str):
        if self._m_list:
            self._m_list.clear()
        self._get_movies_id_dict(title)

        for names_title in self._m_dict:
            self._m_list.append(names_title)

        self._m_list.sort()

    def get_full_movie_data(self, title: str) -> tuple:
        id_film = self._m_dict[title]
        try:
            response = self._mr.get_movie(id_film)

            title = response.json()['Title']
            year = response.json()['Year']
            release_date = response.json()['Released']
            runtime = response.json()['Runtime']
            genre = response.json()['Genre']
            actors = response.json()['Actors']
            short_plot = response.json()['Plot']
            image = response.json()['Poster']
            box_office = response.json()['BoxOffice'].replace("$", "\\$")  # KeyError

            completed_message = (f"{Emojis.CLAPPER} Title\\: *{format_str(title)} \\({format_str(year)}\\)*\n_{format_str(short_plot)}_\n\n"
                                 f"Release date\\: *{format_str(release_date)}*\n\n"
                                 f"Genre\\: *{format_str(genre)}*\n\n"
                                 f"Runtime: *{format_str(runtime)}*\n\n"
                                 f"Stars\\: *{format_str(actors)}*\n\n"
                                 f"Box office\\: *{format_str(box_office)}*")
            logging.info(f'[MOVIE_INFO]: Movie data was collected successfully: {title}')
            return image, completed_message

        except Exception as msg:
            logging.warning(f"OOPS, couldn't find desired movie. Error: {msg}")
