import abc


class MediaPlayer(abc.ABC):
    @abc.abstractmethod
    def play(self, audio_type: str, filename: str):
        pass