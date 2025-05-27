import pygame
from game_settings import FONT, WHITE

class InputBox:
    def __init__(self, x, y, w, h, text='', dynamic_width=True, editable=True):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.txt_surface = FONT.render(text, True, WHITE)
        self.active = False
        self.dynamic_width = dynamic_width
        self.editable = editable

    def handle_event(self, event):
        if not self.editable:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = (225, 0, 0) if self.active else WHITE
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, WHITE)

    def update(self):
        if self.dynamic_width:
            self.rect.w = self.txt_surface.get_width() + 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=5)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def clear(self):
        self.text = ''
        self.txt_surface = FONT.render('', True, WHITE)

    def set_text(self, text):
        self.text = text
        self.txt_surface = FONT.render(text, True, WHITE)
import pygame
from game_settings import FONT, WHITE

class InputBox:
    def __init__(self, x, y, w, h, text='', dynamic_width=True, editable=True):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.txt_surface = FONT.render(text, True, WHITE)
        self.active = False
        self.dynamic_width = dynamic_width
        self.editable = editable

    def handle_event(self, event):
        if not self.editable:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = (225, 0, 0) if self.active else WHITE
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, WHITE)

    def update(self):
        if self.dynamic_width:
            self.rect.w = self.txt_surface.get_width() + 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=5)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def clear(self):
        self.text = ''
        self.txt_surface = FONT.render('', True, WHITE)

    def set_text(self, text):
        self.text = text
        self.txt_surface = FONT.render(text, True, WHITE)