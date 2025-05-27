import pygame
from python_quiz_creator_game_oop.interactive_quiz_game_creator_oop.game_states import Game

def main():
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
