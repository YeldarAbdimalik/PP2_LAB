import pygame

class Ball:
    def __init__(self, x, y, radius, speed, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # границы экрана
        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (15, 47, 67), (self.x, self.y), self.radius)