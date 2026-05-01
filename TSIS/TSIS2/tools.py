import pygame

class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action

    def draw(self, screen, font, active=False):
        color = (180, 180, 180) if not active else (100, 200, 100)

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        text_surf = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surf, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    w, h = surface.get_size()
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= w or y < 0 or y >= h:
            continue

        if surface.get_at((x, y)) == target_color:
            surface.set_at((x, y), new_color)

            stack.append((x+1, y))
            stack.append((x-1, y))
            stack.append((x, y+1))
            stack.append((x, y-1))