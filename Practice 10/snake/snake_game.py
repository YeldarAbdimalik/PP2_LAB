import pygame
import random

pygame.init()

# ====== класс игры ======
class SnakeGame:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.cell = 20

        self.reset()

        self.started = False
        self.game_over = False

    def reset(self):
        self.snake = [
            (300, 300),
            (280, 300),
            (260, 300)
        ]
        self.direction = (self.cell, 0)

        self.food = self.new_food()

        self.score = 0
        self.level = 1
        self.speed = 16

        self.game_over = False

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
            self.game_over = True
            return

        # столкновение с собой
        if head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = self.new_food()

            if self.score % 3 == 0:
                self.level += 1
                self.speed += 1
        else:
            self.snake.pop()

    def draw_grid(self, screen):
        for x in range(0, self.WIDTH, self.cell):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, self.cell):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (self.WIDTH, y))

    def draw(self, screen, font):
        screen.fill((20, 20, 20))

        # сетка
        self.draw_grid(screen)

        # змейка
        for i, s in enumerate(self.snake):
            color = (0, max(50, 255 - i * 15), 0)
            pygame.draw.rect(screen, color, (*s, self.cell, self.cell), border_radius=6)

        # еда
        pygame.draw.rect(screen, (255, 60, 60), (*self.food, self.cell, self.cell), border_radius=6)

        # текст
        text = font.render(f"Score: {self.score}   Level: {self.level}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # ===== меню =====
        if not self.started:
            title = font.render("SNAKE GAME", True, (0, 255, 0))
            info = font.render("Press P to Start", True, (200, 200, 200))

            screen.blit(title, (self.WIDTH//2 - 110, self.HEIGHT//2 - 50))
            screen.blit(info, (self.WIDTH//2 - 120, self.HEIGHT//2))

        elif self.game_over:
            over = font.render("GAME OVER", True, (255, 50, 50))
            retry = font.render("Press P to Restart", True, (200, 200, 200))

            screen.blit(over, (self.WIDTH//2 - 110, self.HEIGHT//2 - 50))
            screen.blit(retry, (self.WIDTH//2 - 140, self.HEIGHT//2))


# ====== main ======
def main():
    try:
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Snake Game")

        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Arial", 24)

        game = SnakeGame()

        running = True
        while running:
            clock.tick(max(game.speed, 5))  # защита от 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if not game.started:
                            game.started = True
                        else:
                            game.reset()
                            game.started = True
                            game.game_over = False

            keys = pygame.key.get_pressed()

            if game.started and not game.game_over:
                game.handle_keys(keys)
                game.update()

            game.draw(screen, font)
            pygame.display.flip()

        pygame.quit()

    except Exception as e:
        print("ERROR:", e)
        input("Press Enter to close...")

    pygame.quit()


if __name__ == "__main__":
    main()