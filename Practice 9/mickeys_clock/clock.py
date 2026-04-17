import pygame
import datetime
import os

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)

        base = os.path.dirname(__file__)

        self.body = pygame.image.load(os.path.join(base, "images", "clock_body.png"))
        self.minute = pygame.image.load(os.path.join(base, "images", "minute_hand.png"))
        self.second = pygame.image.load(os.path.join(base, "images", "second_hand.png"))

        self.body = pygame.transform.scale(self.body, (500, 500))
        self.minute = pygame.transform.scale(self.minute, (190, 190))
        self.second = pygame.transform.scale(self.second, (280, 280))

    def draw_hand(self, img, angle):
        rotated = pygame.transform.rotate(img, angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def draw(self):
        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        minute_angle = -(minutes * 6 + seconds * 0.1)
        second_angle = -(seconds * 6)

        # фон
        body_rect = self.body.get_rect(center=self.center)
        self.screen.blit(self.body, body_rect)

        # стрелки
        self.draw_hand(self.minute, minute_angle)
        self.draw_hand(self.second, second_angle)