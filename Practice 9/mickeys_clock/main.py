import pygame
from clock import Clock

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock = pygame.time.Clock()
game_clock = Clock(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    game_clock.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()