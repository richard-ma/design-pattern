import abc


class Game:
    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def start_play(self):
        pass

    @abc.abstractmethod
    def end_play(self):
        pass

    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()