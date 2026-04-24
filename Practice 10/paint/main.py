import pygame
from paint_logic import Paint

pygame.init()

screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))

paint = Paint()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        paint.handle_event(event, screen)

    pygame.display.flip()

pygame.quit()