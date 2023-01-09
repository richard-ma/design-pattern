from game import Game


class Football(Game):
    def end_play(self):
        print("Football Game Finished!")

    def start_play(self):
        print("Football Game started! Enjoy the game!")

    def initialize(self):
        print("Football Game initialized! Start playing!")


if __name__ == "__main__":
    game = Football()
    game.play()