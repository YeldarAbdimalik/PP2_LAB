import pygame
from ball import Ball

pygame.init()

# ===== экран =====
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

clock = pygame.time.Clock()

# ===== шар =====
ball = Ball(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    radius=25,
    speed=20,
    screen_width=WIDTH,
    screen_height=HEIGHT
)

running = True

# ===== game loop =====
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-ball.speed, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(ball.speed, 0)
            elif event.key == pygame.K_UP:
                ball.move(0, -ball.speed)
            elif event.key == pygame.K_DOWN:
                ball.move(0, ball.speed)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()