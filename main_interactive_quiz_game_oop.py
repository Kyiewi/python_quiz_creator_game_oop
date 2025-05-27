import pygame
from python_quiz_creator_game_oop.game_states import Game

def main():
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
