from mediaplayer import MediaPlayer
from mediaadapter import MediaAdapter


class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, filename: str):
        audio_type = audio_type.lower()

        if audio_type == 'mp3':
            print("Playing mp3 file. Name:", filename)
        elif audio_type == 'vlc' or audio_type == 'mp4':
            mediaAdapter = MediaAdapter(audio_type)
            mediaAdapter.play(audio_type, filename)
        else:
            print("Invalid Media.", audio_type, "format not supported.")


if __name__ == "__main__":
    player = AudioPlayer()
    player.play("mp3", "filenmae.mp3")
    player.play("vlc", "filenmae.vlc")
    player.play("mp4", "filenmae.mp4")
    # invalid media
    player.play("avi", "filenmae.avi")