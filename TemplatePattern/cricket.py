from game import Game


class Cricket(Game):
    def end_play(self):
        print("Cricket Game Finished!")

    def start_play(self):
        print("Cricket Game started! Enjoy the game!")

    def initialize(self):
        print("Cricket Game initialized! Start playing!")


if __name__ == "__main__":
    game = Cricket()
    game.play()