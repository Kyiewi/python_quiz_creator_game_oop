import pygame

# Screen settings
WIDTH, HEIGHT = 1060, 550

# Colors
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont("Courier", 25)
SMALL_FONT = pygame.font.SysFont("Courier", 20)

# Result timer
RESULT_TIMER = pygame.USEREVENT + 2
