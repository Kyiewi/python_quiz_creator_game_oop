import pygame
import sys
from pygame.constants import USEREVENT
from load_assets import *
from input_box import InputBox
from game_states import GameState

class QuizGame:
    def __init__(self):
        self.Screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Quiz Creator")

        self.Clock = pygame.time.Clock()

        self.GameState = GameState.Start
        self.StartFrameIndex = 0
        self.LoadingFrameIndex = 0
        self.SavedMessage = ''
        self.SaveTimestamp = 0

        self.InputBoxes = [
            InputBox(72, 61, 40, 40, DynamicWidth=False),
            InputBox(136, 66, 200, 40),
            InputBox(214, 165, 200, 40),
            InputBox(220, 267, 200, 40),
            InputBox(495, 164, 200, 40),
            InputBox(499, 267, 200, 40),
            InputBox(427, 368, 80, 40, DynamicWidth=False),
        ]

        self.StartButton = pygame.Rect(319, 320, 200, 50)
        self.EnterButton = pygame.Rect(201, 470, 150, 50)
        self.QuitButton = pygame.Rect(500, 470, 150, 50)
        self.YesButton = pygame.Rect(152, 371, 190, 65)
        self.NoButton = pygame.Rect(494, 371, 190, 65)

    def Run(self):
        Running = True
        while Running:
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    Running = False

                if Event.type == pygame.MOUSEBUTTONDOWN:
                    self.HandleMouseClick(Event.pos)

                if Event.type == USEREVENT + 1:
                    pygame.quit()
                    sys.exit()

                if self.GameState == GameState.Quiz:
                    for Box in self.InputBoxes:
                        Box.HandleEvent(Event)

            self.UpdateScreen()
            pygame.display.flip()
            self.Clock.tick(15)

        pygame.quit()
        sys.exit()

    def HandleMouseClick(self, Position):
        if self.GameState == GameState.Start and self.StartButton.collidepoint(Position):
            ClickSound.play()
            self.GameState = GameState.Loading
            self.LoadingFrameIndex = 0

        elif self.GameState == GameState.Quiz:
            if self.EnterButton.collidepoint(Position):
                ClickSound.play()
                with open('quiz_data.txt', 'a') as File:
                    File.write(f"Number:{self.InputBoxes[0].Text}\n")
                    File.write(f"Question:{self.InputBoxes[1].Text}\n")
                    File.write(f"A:{self.InputBoxes[2].Text}\n")
                    File.write(f"B:{self.InputBoxes[3].Text}\n")
                    File.write(f"C:{self.InputBoxes[4].Text}\n")
                    File.write(f"D:{self.InputBoxes[5].Text}\n")
                    File.write(f"Correct Answer:{self.InputBoxes[6].Text}\n")
                self.SavedMessage = 'Saved!'
                self.SaveTimestamp = pygame.time.get_ticks()
                for Box in self.InputBoxes:
                    Box.Clear()

            elif self.QuitButton.collidepoint(Position):
                ClickSound.play()
                self.GameState = GameState.ExitConfirm

        elif self.GameState == GameState.ExitConfirm:
            if self.YesButton.collidepoint(Position):
                ClickSound.play()
                self.GameState = GameState.Sad
                pygame.time.set_timer(USEREVENT + 1, 2000)
            elif self.NoButton.collidepoint(Position):
                ClickSound.play()
                self.GameState = GameState.Quiz

    def UpdateScreen(self):
        self.Screen.fill(BlackColor)

        if self.GameState == GameState.Start:
            self.Screen.blit(StartImages[self.StartFrameIndex], (0, 0))
            pygame.time.delay(80)
            self.StartFrameIndex = (self.StartFrameIndex + 1) % len(StartImages)

        elif self.GameState == GameState.Loading:
            if self.LoadingFrameIndex < len(LoadingImages):
                self.Screen.blit(LoadingImages[self.LoadingFrameIndex], (0, 0))
                pygame.time.delay(120)
                self.LoadingFrameIndex += 1
            else:
                self.GameState = GameState.Quiz

        elif self.GameState == GameState.Quiz:
            self.Screen.blit(QuizTemplateImage, (0, 0))
            for Box in self.InputBoxes:
                Box.Update()
                Box.Draw(self.Screen)

            if self.SavedMessage and pygame.time.get_ticks() - self.SaveTimestamp < 2000:
                SavedTextSurface = SmallFont.render(self.SavedMessage, True, WhiteColor)
                self.Screen.blit(SavedTextSurface, (WIDTH // 2 - SavedTextSurface.get_width() // 2, HEIGHT - 50))
            else:
                self.SavedMessage = ''

        elif self.GameState == GameState.ExitConfirm:
            self.Screen.blit(ExitImage, (0, 0))

        elif self.GameState == GameState.Sad:
            self.Screen.blit(SadImage, (0, 0))
