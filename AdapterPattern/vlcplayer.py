from advancedmediaplayer import AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename: str):
        print("Playing vlc file. Name:", filename)

    def play_mp4(self, filename: str):
        pass


if __name__ == "__main__":
    p = VlcPlayer()
    p.play_vlc("filename")
    p.play_mp4("filename")