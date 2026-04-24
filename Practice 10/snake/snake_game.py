import pygame
import random

class SnakeGame:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.cell = 20

        # стартовая змейка (длина 3)
        self.snake = [
            (300, 300),
            (280, 300),
            (260, 300)
        ]

        self.direction = (self.cell, 0)

        self.food = self.new_food()

        self.score = 0
        self.level = 1
        self.speed = 8

    def new_food(self):
        while True:
            f = (
                random.randrange(0, self.WIDTH, self.cell),
                random.randrange(0, self.HEIGHT, self.cell)
            )
            if f not in self.snake:
                return f

    def handle_keys(self, keys):
        if keys[pygame.K_UP] and self.direction != (0, self.cell):
            self.direction = (0, -self.cell)
        if keys[pygame.K_DOWN] and self.direction != (0, -self.cell):
            self.direction = (0, self.cell)
        if keys[pygame.K_LEFT] and self.direction != (self.cell, 0):
            self.direction = (-self.cell, 0)
        if keys[pygame.K_RIGHT] and self.direction != (-self.cell, 0):
            self.direction = (self.cell, 0)

    def update(self):
        head = (
            self.snake[0][0] + self.direction[0],
            self.snake[0][1] + self.direction[1]
        )

        # столкновение со стеной
        if head[0] < 0 or head[0] >= self.WIDTH or head[1] < 0 or head[1] >= self.HEIGHT:
            return False

        # столкновение с собой
        if head in self.snake:
            return False

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = self.new_food()

            if self.score % 3 == 0:
                self.level += 1
                self.speed += 1
        else:
            self.snake.pop()

        return True

    def draw_grid(self, screen):
        for x in range(0, self.WIDTH, self.cell):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, self.cell):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (self.WIDTH, y))

    def draw(self, screen, font):
        screen.fill((20, 20, 20))

        # сетка
        self.draw_grid(screen)

        # змейка (градиент)
        for i, s in enumerate(self.snake):
            color = (0, 255 - i*10, 0)
            pygame.draw.rect(screen, color, (*s, self.cell, self.cell), border_radius=5)

        # еда
        pygame.draw.rect(screen, (255, 50, 50), (*self.food, self.cell, self.cell), border_radius=5)

        # текст
        text = font.render(f"Score: {self.score}   Level: {self.level}", True, (255, 255, 255))
        screen.blit(text, (10, 10))