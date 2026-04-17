import pygame
import os
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

# ===== ПУТИ =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
music_folder = os.path.join(BASE_DIR, "music")

# Проверка папки
if not os.path.exists(music_folder):
    print("Ошибка: папка music не найдена")
    exit()

# ===== ПЛЕЙЛИСТ =====
playlist = [
    os.path.join(music_folder, f)
    for f in os.listdir(music_folder)
    if f.endswith((".mp3", ".wav"))
]

if len(playlist) == 0:
    print("В папке music нет аудиофайлов")
    exit()

# ===== ПЛЕЕР =====
player = MusicPlayer(playlist)

# ===== UI =====
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()
running = True

# ===== LOOP =====
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.previous()
            elif event.key == pygame.K_q:
                running = False

    # ===== ТЕКСТ =====
    track_name = os.path.basename(player.get_current_track())

    track_text = font.render(f"Track: {track_name}", True, (255, 255, 255))
    screen.blit(track_text, (50, 120))

    status = "Playing" if player.playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (200, 200, 200))
    screen.blit(status_text, (50, 160))

    help_text = font.render("P Play | S Stop | N Next | B Back | Q Quit", True, (180, 180, 180))
    screen.blit(help_text, (50, 220))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()