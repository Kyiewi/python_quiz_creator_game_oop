import pygame
import random
import sys
from game_settings import WIDTH, HEIGHT, WHITE, BLACK, SMALL_FONT, RESULT_TIMER
from input_box import InputBox
from python_quiz_creator_game_oop.game_assets import load_assets, load_background_music

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Quiz Game")

        self.assets = load_assets()
        load_background_music()
        self.click_sound = self.assets["click_sound"]

        self.clock = pygame.time.Clock()

        self.boxes = [
            InputBox(43,  34, 40, 40, dynamic_width=False),
            InputBox(117, 38, 200, 40),
            InputBox(171, 158, 200, 40),
            InputBox(178, 286, 200, 40),
            InputBox(615, 164, 200, 40),
            InputBox(625, 287, 200, 40),
            InputBox(645, 392, 80, 40, dynamic_width=False),
        ]
        self.answer_input = InputBox(645, 392, 80, 40, dynamic_width=False, editable=True)

        self.create_button = pygame.Rect(407, 320, 200, 50)
        self.play_button = pygame.Rect(454, 390, 200, 50)
        self.enter_button = pygame.Rect(201, 470, 150, 50)
        self.quit_button = pygame.Rect(807, 470, 150, 50)
        self.submit_button = pygame.Rect(120, 483, 150, 50)
        self.back_button = pygame.Rect(469, 476, 150, 50)
        self.yes_button = pygame.Rect(251, 388, 190, 65)
        self.no_button = pygame.Rect(728, 371, 190, 65)

        self.showing_start = True
        self.showing_create = False
        self.showing_exit_confirm = False
        self.showing_sad = False
        self.showing_answer = False
        self.showing_result = False
        self.showing_loading = False
        self.loading_target = None

        self.saved_msg = ''
        self.save_time = 0
        self.is_correct = False
        self.current_question = []
        self.timer_set = False

        self.start_frame = 0
        self.load_frame = 0

    def load_random_question(self):
        try:
            with open("quiz_data.txt") as file:
                parts = file.read().strip().split("Number:")
                question_blocks = [p for p in parts if p.strip()]
                return random.choice(question_blocks).splitlines()
        except:
            return []

    def run(self):
        while True:
            self.handle_events()
            self.draw_screen()
            self.clock.tick(15)

            if self.showing_result and not self.timer_set:
                pygame.time.set_timer(RESULT_TIMER, 3000)
                self.timer_set = True
            if not self.showing_result:
                self.timer_set = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == RESULT_TIMER and self.showing_result:
                pygame.time.set_timer(RESULT_TIMER, 0)
                self.current_question = self.load_random_question()
                for index, line in enumerate(self.current_question[:6]):
                    if ':' in line:
                        _, value = line.split(':', 1)
                        self.boxes[index].set_text(value.strip())
                self.answer_input.clear()
                self.showing_result = False
                self.showing_answer = True

            if event.type == pygame.USEREVENT + 1:
                pygame.quit()
                sys.exit()

            if self.showing_create:
                for box in self.boxes:
                    box.handle_event(event)
            if self.showing_answer:
                self.answer_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse(event)

    def handle_mouse(self, event):
        if self.showing_start:
            if self.create_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_start = False
                self.showing_loading = True
                self.loading_target = "create"
                self.load_frame = 0
            elif self.play_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_start = False
                self.showing_loading = True
                self.loading_target = "play"
                self.load_frame = 0

        elif self.showing_create:
            if self.enter_button.collidepoint(event.pos):
                self.click_sound.play()
                with open("quiz_data.txt", "a") as file:
                    for index, label in enumerate(["Number", "Question", "A", "B", "C", "D", "Correct Answer"]):
                        file.write(f"{label}:{self.boxes[index].text}\n")
                self.saved_msg = "Saved!"
                self.save_time = pygame.time.get_ticks()
                for box in self.boxes:
                    box.clear()
            elif self.back_button.collidepoint(event.pos):
                self.click_sound.play()
                for box in self.boxes:
                    box.clear()
                self.showing_create = False
                self.showing_start = True
            elif self.quit_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_create = False
                self.showing_exit_confirm = True

        elif self.showing_answer:
            if self.submit_button.collidepoint(event.pos):
                self.click_sound.play()
                correct = next((line.split(':', 1)[1].strip() for line in self.current_question if line.startswith("Correct Answer:")), "")
                self.is_correct = (self.answer_input.text.strip().lower() == correct.lower())
                self.showing_answer = False
                self.showing_result = True
            elif self.back_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_answer = False
                self.showing_start = True
            elif self.quit_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_answer = False
                self.showing_exit_confirm = True

        elif self.showing_exit_confirm:
            if self.yes_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_exit_confirm = False
                self.showing_sad = True
                pygame.time.set_timer(pygame.USEREVENT + 1, 2000)
            elif self.no_button.collidepoint(event.pos):
                self.click_sound.play()
                self.showing_exit_confirm = False
                self.showing_create = True

    def draw_screen(self):
        self.screen.fill(BLACK)

        if self.showing_start:
            self.screen.blit(self.assets["start_images"][self.start_frame], (0, 0))
            pygame.time.delay(80)
            self.start_frame = (self.start_frame + 1) % len(self.assets["start_images"])

        elif self.showing_loading:
            if self.load_frame < len(self.assets["loading_images"]):
                self.screen.blit(self.assets["loading_images"][self.load_frame], (0, 0))
                pygame.time.delay(120)
                self.load_frame += 1
            else:
                self.showing_loading = False
                if self.loading_target == "create":
                    self.showing_create = True
                    for box in self.boxes:
                        box.clear()
                elif self.loading_target == "play":
                    self.current_question = self.load_random_question()
                    for index, line in enumerate(self.current_question[:6]):
                        if ':' in line:
                            _, value = line.split(':', 1)
                            self.boxes[index].set_text(value.strip())
                    self.answer_input.clear()
                    self.showing_answer = True
                self.loading_target = None

        elif self.showing_create:
            self.screen.blit(self.assets["quiz_template"], (0, 0))
            for box in self.boxes:
                box.update()
                box.draw(self.screen)
            if self.saved_msg and pygame.time.get_ticks() - self.save_time < 2000:
                self.screen.blit(SMALL_FONT.render(self.saved_msg, True, WHITE), (WIDTH // 2 - 50, HEIGHT - 50))

        elif self.showing_answer:
            self.screen.blit(self.assets["quiz_template"], (0, 0))
            for index in range(6):
                self.screen.blit(self.boxes[index].txt_surface, (self.boxes[index].rect.x + 5, self.boxes[index].rect.y + 5))
            self.answer_input.update()
            self.answer_input.draw(self.screen)

        elif self.showing_result:
            self.screen.blit(self.assets["correct"] if self.is_correct else self.assets["wrong"], (0, 0))

        elif self.showing_exit_confirm:
            self.screen.blit(self.assets["exit"], (0, 0))

        elif self.showing_sad:
            self.screen.blit(self.assets["sad"], (0, 0))

        pygame.display.flip()