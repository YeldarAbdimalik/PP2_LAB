import pygame
from game import Game

pygame.init()

game = Game()

screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    game.move_player(keys)
    game.spawn_coins()
    game.update_coins()
    game.draw(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()