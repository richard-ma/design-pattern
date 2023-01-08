from user import User


if __name__ == "__main__":
    robert = User("Robert")
    john = User("John")

    robert.send_message("Hi John!")
    john.send_message("Hello Robert!")