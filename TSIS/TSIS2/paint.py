import pygame
import datetime
from tools import Button, flood_fill

pygame.init()

WIDTH, HEIGHT = 800, 600
UI_WIDTH = 220
DRAW_WIDTH = WIDTH - UI_WIDTH

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint (Fixed)")

font = pygame.font.SysFont("Arial", 16)


class Paint:
    def __init__(self):
        self.color = (0, 0, 0)
        self.radius = 2
        self.mode = "draw"

        self.start_pos = None
        self.last_pos = None
        self.drawing = False

        self.text_input = ""
        self.text_pos = None
        self.typing = False
        self.font = pygame.font.SysFont("Arial", 20)

    def to_canvas(self, pos):
        return (pos[0] - UI_WIDTH, pos[1])

    def handle_event(self, event, canvas):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_c:
                canvas.fill((255, 255, 255))

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("image_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            if self.typing:
                if event.key == pygame.K_RETURN:
                    txt = self.font.render(self.text_input, True, self.color)
                    canvas.blit(txt, self.text_pos)
                    self.typing = False

                elif event.key == pygame.K_ESCAPE:
                    self.typing = False

                elif event.key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]

                else:
                    self.text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > UI_WIDTH:

                pos = self.to_canvas(event.pos)

                if self.mode == "fill":
                    flood_fill(canvas, pos[0], pos[1], self.color)
                    return

                if self.mode == "text":
                    self.text_pos = pos
                    self.typing = True
                    self.text_input = ""
                    return

                self.start_pos = pos
                self.last_pos = pos
                self.drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if self.start_pos and event.pos[0] > UI_WIDTH:
                pos = self.to_canvas(event.pos)

                if self.mode == "rect":
                    pygame.draw.rect(
                        canvas,
                        self.color,
                        pygame.Rect(
                            self.start_pos[0],
                            self.start_pos[1],
                            pos[0] - self.start_pos[0],
                            pos[1] - self.start_pos[1]
                        ),
                        self.radius
                    )

                if self.mode == "circle":
                    radius = int(((pos[0]-self.start_pos[0])**2 + (pos[1]-self.start_pos[1])**2) ** 0.5)
                    pygame.draw.circle(canvas, self.color, self.start_pos, radius, self.radius)

                if self.mode == "line":
                    pygame.draw.line(canvas, self.color, self.start_pos, pos, self.radius)

            self.drawing = False
            self.last_pos = None

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and event.pos[0] > UI_WIDTH:
                pos = self.to_canvas(event.pos)

                if self.mode == "draw":
                    if self.last_pos:
                        pygame.draw.line(canvas, self.color, self.last_pos, pos, self.radius)
                    self.last_pos = pos

                if self.mode == "eraser":
                    pygame.draw.circle(canvas, (255, 255, 255), pos, self.radius)


def main():
    clock = pygame.time.Clock()
    paint = Paint()

    canvas = pygame.Surface((DRAW_WIDTH, HEIGHT))
    canvas.fill((255, 255, 255))

    buttons = [
        Button(10,20,180,30,"Draw","draw"),
        Button(10,60,180,30,"Eraser","eraser"),
        Button(10,100,180,30,"Rect","rect"),
        Button(10,140,180,30,"Circle","circle"),
        Button(10,180,180,30,"Line","line"),
        Button(10,220,180,30,"Fill","fill"),
        Button(10,260,180,30,"Text","text"),

        Button(10,320,180,30,"Small",2),
        Button(10,360,180,30,"Medium",5),
        Button(10,400,180,30,"Large",10),
    ]

    colors = [
        ((0,0,0),(10,460)),
        ((255,0,0),(60,460)),
        ((0,255,0),(110,460)),
        ((0,0,255),(160,460)),
        ((255,255,0),(10,510))
    ]

    running = True
    while running:
        screen.fill((200,200,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.is_clicked(event.pos):
                        if isinstance(b.action, str):
                            paint.mode = b.action
                        if isinstance(b.action, int):
                            paint.radius = b.action

                for color, pos in colors:
                    rect = pygame.Rect(pos[0], pos[1], 40, 40)
                    if rect.collidepoint(event.pos):
                        paint.color = color

            paint.handle_event(event, canvas)

        temp = canvas.copy()

        if paint.drawing and paint.mode == "line":
            mouse = pygame.mouse.get_pos()
            if mouse[0] > UI_WIDTH:
                pos = (mouse[0]-UI_WIDTH, mouse[1])
                pygame.draw.line(temp, paint.color, paint.start_pos, pos, paint.radius)

        if paint.drawing and paint.mode == "rect":
            mouse = pygame.mouse.get_pos()
            if mouse[0] > UI_WIDTH:
                pos = (mouse[0]-UI_WIDTH, mouse[1])
                pygame.draw.rect(
                    temp,
                    paint.color,
                    pygame.Rect(
                        paint.start_pos[0],
                        paint.start_pos[1],
                        pos[0]-paint.start_pos[0],
                        pos[1]-paint.start_pos[1]
                    ),
                    paint.radius
                )

        if paint.drawing and paint.mode == "circle":
            mouse = pygame.mouse.get_pos()
            if mouse[0] > UI_WIDTH:
                pos = (mouse[0] - UI_WIDTH, mouse[1])

                radius = int(((pos[0]-paint.start_pos[0])**2 +
                        (pos[1]-paint.start_pos[1])**2) ** 0.5)
                radius = max(1, radius)
                pygame.draw.circle(
                temp,
                paint.color,
                paint.start_pos,
                radius,
                paint.radius
        )

        if paint.typing:
            txt = paint.font.render(paint.text_input, True, paint.color)
            temp.blit(txt, paint.text_pos)

        screen.blit(temp, (UI_WIDTH, 0))

        pygame.draw.line(screen,(0,0,0),(UI_WIDTH,0),(UI_WIDTH,HEIGHT),2)

        for b in buttons:
            active = False
            if isinstance(b.action,str) and paint.mode == b.action:
                active = True
            if isinstance(b.action,int) and paint.radius == b.action:
                active = True
            b.draw(screen,font,active)

        for color, pos in colors:
            pygame.draw.rect(screen, color, (*pos,40,40))
            pygame.draw.rect(screen,(0,0,0),(*pos,40,40),2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()