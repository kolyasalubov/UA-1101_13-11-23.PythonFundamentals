import logging

import telebot
from telebot import types

from RiznychokAnna.Demo.configuration.configurator import Config
from movie_info import MovieInfo

from RiznychokAnna.Demo.utils.constants import Emojis
from RiznychokAnna.Demo.utils.utils import setup_logs


if __name__ == '__main__':
    setup_logs()
    config = Config()

    bot = telebot.TeleBot(config.get_bot_token())
    movie_handler = MovieInfo()

    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        bot.reply_to(message=message,
                     text=f"Hello, {user.first_name}!\nSend a title of movie you'd like to find extended information.")


    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text not in movie_handler.get_movies_list():
            movie_handler.create_movie_titles_list(message.text)
            buttons = []
            keyboard = types.ReplyKeyboardMarkup()

            for mov in movie_handler.get_movies_list():
                buttons.append(types.KeyboardButton(mov))
                if len(buttons) > 1:
                    keyboard.row(*buttons)
                    buttons = []

            keyboard.row(*buttons)
            bot.send_message(chat_id=message.from_user.id,
                             text=Emojis.CLAPPER + ' Choose a movie from list below:',
                             reply_markup=keyboard)
        elif message.text in movie_handler.get_movies_list():
            message_to_send = movie_handler.get_full_movie_data(message.text)
            bot.send_photo(chat_id=message.from_user.id,
                           photo=message_to_send[0],
                           caption=message_to_send[1],
                           parse_mode="MarkdownV2")
            logging.info(f'[BOT]: Successfully send information about movies to the user')

    bot.polling(none_stop=True, interval=0)
