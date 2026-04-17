import pygame

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current = 0
        self.playing = False

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play()
        self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play()

    def previous(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        return self.playlist[self.current]