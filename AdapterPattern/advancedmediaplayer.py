import abc


class AdvancedMediaPlayer(abc.ABC):
    @abc.abstractmethod
    def play_vlc(self, filename: str):
        pass

    @abc.abstractmethod
    def play_mp4(self, filename: str):
        pass