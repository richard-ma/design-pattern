from observer import Observer


class OctalObserver(Observer):
    def __init__(self, subject: "Subject"):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Octal String:", str(oct(self._subject.get_state())))