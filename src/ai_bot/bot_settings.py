from ..ai_bot.bot_API import BOT_API_KEY

import openai


class BotSettings:
    def __init__(self, temperature=0.5, max_tokens=500, bot_model='gpt-3.5-turbo', api_key=BOT_API_KEY):
        self.__temperature = temperature
        self.__max_tokens = max_tokens
        self.__bot_model = bot_model
        self.__API_KEY = api_key

        openai.api_key = self.__API_KEY

    def get_temperature(self):
        return self.__temperature

    def get_max_tokens(self):
        return self.__max_tokens

    def get_bot_model(self):
        return self.__bot_model

    def get_API_KEY(self):
        return self.__API_KEY


# print(BotSettings.get_bot_model)