import pygame

pygame.init()

# ===== настройки экрана =====
WIDTH, HEIGHT = 800, 600
DRAW_WIDTH = WIDTH // 2  # половина экрана для рисования

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

font = pygame.font.SysFont("Arial", 18)

# ===== класс Paint =====
class Paint:
    def __init__(self):
        self.color = (0, 0, 0)
        self.radius = 5
        self.mode = "draw"
        self.start_pos = None

    def handle_event(self, event, canvas):
        # ===== клавиши =====
        if event.type == pygame.KEYDOWN:
            # режимы
            if event.key == pygame.K_r:
                self.mode = "rect"
            if event.key == pygame.K_o:
                self.mode = "circle"
            if event.key == pygame.K_e:
                self.mode = "eraser"
            if event.key == pygame.K_d:
                self.mode = "draw"

            # цвета
            if event.key == pygame.K_1:
                self.color = (0, 0, 0)      # черный
            if event.key == pygame.K_2:
                self.color = (255, 0, 0)    # красный
            if event.key == pygame.K_3:
                self.color = (0, 255, 0)    # зеленый
            if event.key == pygame.K_4:
                self.color = (0, 0, 255)    # синий
            if event.key == pygame.K_5:
                self.color = (255, 255, 0)  # желтый

            # размер кисти
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                self.radius += 1
            if event.key == pygame.K_MINUS:
                self.radius = max(1, self.radius - 1)

            # очистка
            if event.key == pygame.K_c:
                canvas.fill((255, 255, 255))

        # ===== мышка =====
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < DRAW_WIDTH:  # только в зоне рисования
                self.start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if self.start_pos and event.pos[0] < DRAW_WIDTH:
                if self.mode == "rect":
                    pygame.draw.rect(canvas, self.color,
                                     (*self.start_pos,
                                      event.pos[0] - self.start_pos[0],
                                      event.pos[1] - self.start_pos[1]), 2)

                if self.mode == "circle":
                    pygame.draw.circle(canvas, self.color,
                                       self.start_pos, 50, 2)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if event.pos[0] < DRAW_WIDTH:
                    if self.mode == "draw":
                        pygame.draw.circle(canvas, self.color, event.pos, self.radius)
                    if self.mode == "eraser":
                        pygame.draw.circle(canvas, (255, 255, 255), event.pos, self.radius)


# ===== основной цикл =====
def main():
    clock = pygame.time.Clock()

    paint = Paint()

    # отдельная поверхность для рисования
    canvas = pygame.Surface((DRAW_WIDTH, HEIGHT))
    canvas.fill((0      , 0, 0))

    running = True
    while running:
        screen.fill((200, 200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            paint.handle_event(event, canvas)

        # рисуем холст
        screen.blit(canvas, (0, 0))

        # линия разделения
        pygame.draw.line(screen, (0, 0, 0), (DRAW_WIDTH, 0), (DRAW_WIDTH, HEIGHT), 2)

        # ===== UI справа =====
        ui_x = DRAW_WIDTH + 10

        info = [
            "Modes:",
            "D - draw",
            "E - eraser",
            "R - rectangle",
            "O - circle",
            "",
            "Colors:",
            "1 - black",
            "2 - red",
            "3 - green",
            "4 - blue",
            "5 - yellow",
            "",
            "Size:",
            "+ / -",
            "",
            "C - clear"
        ]

        for i, line in enumerate(info):
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (ui_x, 20 + i * 20))

        # текущий цвет
        pygame.draw.rect(screen, paint.color, (ui_x, 350, 50, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()