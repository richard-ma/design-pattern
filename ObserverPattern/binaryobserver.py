from observer import Observer


class BinaryObserver(Observer):
    def __init__(self, subject: "Subject"):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Binary String:", str(bin(self._subject.get_state())))