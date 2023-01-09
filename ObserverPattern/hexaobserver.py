from observer import Observer


class HexaObserver(Observer):
    def __init__(self, subject: "Subject"):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Hex String:", str(hex(self._subject.get_state())).upper())