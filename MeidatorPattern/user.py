from chatroom import ChatRoom


class User:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    def send_message(self, message: str):
        ChatRoom.show_message(self, message)