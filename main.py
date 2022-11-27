import datetime
import random
from typing import List


class Chatroom:
    def __init__(self, messages: List, size: int = 5):
        self.size = size
        self.messages = messages

    def receive_message(self, message):
        self.messages.append(message)
        return True

    def delete_message(self, message_id: int):
        for message in self.messages:
            if int(message['id']) == message_id:
                del message[f'{message_id}']
        return True

    def edit_message(self, message_id: int, updated_message: str):
        for message in self.messages:
            if int(message['id']) == message_id:
                message[f'{message_id}']['message'] = updated_message
        return True


class MessageCreation:
    def __init__(self):
        ...

    @staticmethod
    def create_message(sent_from: str, sent_to: str, message: str = "Empty body."):
        return {
            'id': f'id_{random.randint(0, 9999)}',
            'to': sent_to,
            'from': sent_from,
            'message': message,
            'time': datetime.datetime.time,
        }


class User(MessageCreation):
    """User that will be created that can take a recipient and create
    a message that will be added to the chatroom for everyone to see."""

    def __init__(self, name, username: str = None):
        super().__init__()
        self.name = name
        self.username = username or f'username{random.randint(0, 100)}'

    def create_message_to_send(self, message_to: str, message: str):
        return self.create_message(
            sent_from=self.name,
            sent_to=message_to,
            message=message
        )

    def create_delete_message(self):
        ...

class MessagingApp:
    """Application  that will contain an instance of a
    Chatroom, User, Message classes. Will handle registering
    and giving access? to the users. Create messages on the fly.
    Allow users to submit their own messages. This class is like
    a moderator per se"""

    def __init__(self, my_chatroom: Chatroom, message: MessageCreation, users: List[User]):
        self.chatroom = my_chatroom
        self.user = users
        self.message = message


if __name__ == '__main__':
    chatroom = Chatroom(messages=[],size=100)
    message_ability = MessageCreation()
    user_one = User(name='Emmi', username='penguin')
    user_two = User(name='Chanel', username='chanel25')
    my_messaging_app = MessagingApp(my_chatroom=chatroom, message=message_ability, users=[user_one, user_two])
    


