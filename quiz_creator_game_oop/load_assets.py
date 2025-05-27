import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 850, 550

def LoadAndScale(path):
    return pygame.transform.scale(pygame.image.load(path), (WIDTH, HEIGHT))

# Background Images
QuizTemplateImage = LoadAndScale('ASSET/quiz_template.png')
SadImage = LoadAndScale('ASSET/sad.png')
ExitImage = LoadAndScale('ASSET/Exit.png')

# Animations
StartImages = [LoadAndScale(f'ASSET/START/start ({Index}).png') for Index in range(1, 13)]
LoadingImages = [LoadAndScale(f'ASSET/LOADING/loading ({Index}).png') for Index in range(1, 23)]

# Sounds
ClickSound = pygame.mixer.Sound('SOUNDS/click.mp3')
pygame.mixer.music.load('SOUNDS/background music.mp3')
pygame.mixer.music.play(-1)

# Fonts
MainFont = pygame.font.SysFont("Courier", 25)
SmallFont = pygame.font.SysFont("Courier", 20)

# Colors
WhiteColor = (225, 225, 225)
BlackColor = (0, 0, 0)
