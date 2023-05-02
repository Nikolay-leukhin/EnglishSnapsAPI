from ..ai_bot.bot_message_history import MessageHistory
from ..ai_bot.bot_settings import BotSettings
from ..ai_bot.bot_chooser_request import RequestChooser

from typing import Dict

import openai

from ..schemas.message import BotRoles


class BotAssistant:
    def __init__(self, last_request: dict, setting: BotSettings = BotSettings()) -> None:
        self.settings = setting
        self.messages = MessageHistory(last_request).history
        self.last_request = last_request


    def make_bot_request(self):
        self.messages.append(self.__handle_user_prompt())
        return self.__process_bot_response()

    def __handle_user_prompt(self) -> Dict[str, str]:
        message_model = {
            'role': 'user',
            'content': self.last_request.get('message_text')
        }
        return message_model

    def __process_bot_response(self) -> Dict:
        if self.messages[-1].get('role') != 'user':
            raise ValueError("No user prompt found. You should add a user prompt first.")

        try:
            bot_response = openai.ChatCompletion.create(
                model=self.settings.get_bot_model(),
                messages=self.messages,
                temperature=self.settings.get_temperature(),
                max_tokens=self.settings.get_max_tokens()
            )
            response: dict = {
                'user_id': self.last_request.get('user_id'),
                'session_id': self.last_request.get('session_id'),
                'message_order': self.last_request.get('message_order') + 1,
                'message_text': RequestChooser.get_response(bot_response),
                'sender': BotRoles.assistant,
            }
            return response
        except openai.error.APIError as ex:
            raise ValueError(f"Error occurred while processing the bot response: {ex}")
