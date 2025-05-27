import pygame
from game_settings import WIDTH, HEIGHT

def load_and_scale(path):
    return pygame.transform.scale(pygame.image.load(path), (WIDTH, HEIGHT))

def load_assets():
    return {
        "quiz_template": load_and_scale("../ASSET 2/quiz_template.png"),
        "sad": load_and_scale("../ASSET/sad.png"),
        "exit": load_and_scale("../ASSET/Exit.png"),
        "correct": load_and_scale("../ASSET/correct.png"),
        "wrong": load_and_scale("../ASSET/wrong.png"),
        "start_images": [load_and_scale(f'ASSET 2/START/Start ({i}).png') for i in range(1, 13)],
        "loading_images": [load_and_scale(f'ASSET/LOADING/loading ({i}).png') for i in range(1, 23)],
        "click_sound": pygame.mixer.Sound("SOUNDS/click.mp3")
    }

def load_background_music():
    pygame.mixer.music.load("SOUNDS/background music.mp3")
    pygame.mixer.music.play(-1)