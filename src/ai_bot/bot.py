from typing import Dict

import openai
from .bot_config import BOT_API_KEY


class BotAssistant:
    __temp: float
    __max_tokens: int
    __bot_model = 'gpt-3.5-turbo'
    __API_KEY: str
    messages = [{
        'role': 'system',
        'content': ""
    }]

    def __init__(self, api_key=BOT_API_KEY,
                 bot_temperature=0.5,
                 max_tokens=100,
                 started_role='You help learn English to everyone'
                 ) -> None:

        self.__API_KEY = api_key
        self.__temp = bot_temperature
        self.__max_tokens = max_tokens
        self.messages[0]['content'] = started_role

        openai.api_key = self.__API_KEY

    def make_bot_request(self, user_text) -> str:
        user_prompt = self.__handle_user_prompt(user_text)
        self.messages.append(user_prompt)

        bot_answer = self.__process_bot_response()
        self.messages.append(bot_answer)

        return bot_answer.get('content')

    def __handle_user_prompt(self, text: str) -> Dict[str, str]:
        message_model = {
            'role': 'user',
            'content': text
        }
        return message_model

    def __process_bot_response(self) -> Dict[str, str]:
        if self.messages[-1].get('role') != 'user':
            raise ValueError("No user prompt found. You should add a user prompt first.")

        try:
            bot_response = openai.ChatCompletion.create(
                model=self.__bot_model,
                messages=self.messages,
                temperature=self.__temp,
                max_tokens=self.__max_tokens
            )
            return {
                'role': 'assistant',
                'content': self.format_bot_response(bot_response)
            }
        except openai.error.APIError as ex:
            raise ValueError(f"Error occurred while processing the bot response: {ex}")

    def format_bot_response(self, response):
        return response.get('choices')[0].get('message').get('content')
