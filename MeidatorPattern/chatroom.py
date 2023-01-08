class ChatRoom:
    @staticmethod
    def show_message(user: "User", message: str):
        print("[", user.get_name(), "] :", message)