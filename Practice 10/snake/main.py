import pygame
from snake_game import SnakeGame

pygame.init()

game = SnakeGame()
screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    game.handle_keys(keys)

    running = game.update()

    game.draw(screen, font)

    pygame.display.flip()
    clock.tick(game.speed)

pygame.quit()