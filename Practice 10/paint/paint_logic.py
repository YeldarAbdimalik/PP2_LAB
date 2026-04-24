import pygame

class Paint:
    def __init__(self):
        self.color = (0, 0, 0)
        self.radius = 5
        self.mode = "draw"
        self.start_pos = None

    def handle_event(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.mode = "rect"
            if event.key == pygame.K_c:
                self.mode = "circle"
            if event.key == pygame.K_e:
                self.mode = "eraser"
            if event.key == pygame.K_d:
                self.mode = "draw"

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if self.mode == "rect":
                pygame.draw.rect(screen, self.color,
                                 (*self.start_pos,
                                  event.pos[0] - self.start_pos[0],
                                  event.pos[1] - self.start_pos[1]), 2)

            if self.mode == "circle":
                pygame.draw.circle(screen, self.color, self.start_pos, 50, 2)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if self.mode == "draw":
                    pygame.draw.circle(screen, self.color, event.pos, self.radius)
                if self.mode == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, self.radius)