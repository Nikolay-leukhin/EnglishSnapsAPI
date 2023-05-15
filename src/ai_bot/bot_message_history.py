from ..database import query_get_latest_msgs


class MessageHistory:
    """class that recieving message history"""

    def __init__(self, latest_msg: dict, quantity: int):
        self.cur_user = latest_msg.get('user_id')
        self.cur_session = latest_msg.get('session_id')
        self.quantity = quantity
        self.history = self.get_latest_msgs()
        print(self.history)

    def get_latest_msgs(self):
        raw_history = query_get_latest_msgs(
            quantity=self.quantity,
            user=self.cur_user,
            session_num=self.cur_session
        )

        sorted_history = []
        for item in raw_history:
            sorted_item = {
                'role': item.sender,
                'content': item.message_text
            }
            sorted_history.append(sorted_item)

        return sorted_history

