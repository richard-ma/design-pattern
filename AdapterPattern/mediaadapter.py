from mediaplayer import MediaPlayer
from vlcplayer import VlcPlayer
from mp4player import Mp4Player


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        audio_type = audio_type.lower()

        if audio_type == 'vlc':
            self._advanceMusicPlayer = VlcPlayer()
        elif audio_type == 'mp4':
            self._advanceMusicPlayer = Mp4Player()

    def play(self, audio_type: str, filename: str):
        audio_type = audio_type.lower()

        if audio_type == 'vlc':
            self._advanceMusicPlayer.play_vlc(filename)
        elif audio_type == 'mp4':
            self._advanceMusicPlayer.play_mp4(filename)


if __name__ == "__main__":
    player = MediaAdapter("vlc")
    player.play("vlc", "filename.vlc")

    player = MediaAdapter("mp4")
    player.play("mp4", "filename.mp4")