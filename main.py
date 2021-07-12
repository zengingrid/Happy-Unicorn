from game.controllers.start import GameInitiator

if __name__ == "__main__":
    # This is the main "entrypoint" to the program
    player_name = input("Hey unicorn, what is your name? ")
    game_start = GameInitiator(player_name)
    game_start.run()