import pygame
from load_assets import MainFont, WhiteColor

class InputBox:
    def __init__(self, PositionX, PositionY, Width, Height, Text='', DynamicWidth=True):
        self.Rect = pygame.Rect(PositionX, PositionY, Width, Height)
        self.Color = WhiteColor
        self.Text = Text
        self.TextSurface = MainFont.render(Text, True, WhiteColor)
        self.IsActive = False
        self.DynamicWidth = DynamicWidth

    def HandleEvent(self, Event):
        if Event.type == pygame.MOUSEBUTTONDOWN:
            self.IsActive = self.Rect.collidepoint(Event.pos)
            self.Color = (225, 0, 0) if self.IsActive else WhiteColor

        if Event.type == pygame.KEYDOWN and self.IsActive:
            if Event.key == pygame.K_RETURN:
                self.IsActive = False
            elif Event.key == pygame.K_BACKSPACE:
                self.Text = self.Text[:-1]
            else:
                self.Text += Event.unicode
            self.TextSurface = MainFont.render(self.Text, True, WhiteColor)

    def Update(self):
        if self.DynamicWidth:
            self.Rect.w = self.TextSurface.get_width() + 10

    def Draw(self, Surface):
        pygame.draw.rect(Surface, self.Color, self.Rect, width=2, border_radius=5)
        Surface.blit(self.TextSurface, (self.Rect.x + 5, self.Rect.y + 5))

    def Clear(self):
        self.Text = ''
        self.TextSurface = MainFont.render(self.Text, True, WhiteColor)
