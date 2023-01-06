from advancedmediaplayer import AdvancedMediaPlayer


class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, filename: str):
        pass

    def play_mp4(self, filename: str):
        print("Playing mp4 file. Name:", filename)


if __name__ == "__main__":
    p = Mp4Player()
    p.play_mp4("filename")
    p.play_vlc("filename")