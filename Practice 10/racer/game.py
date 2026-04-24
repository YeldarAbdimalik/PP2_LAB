import pygame
import random

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 400, 600
        self.player = pygame.Rect(180, 500, 40, 60)
        self.speed = 5

        self.coins = []
        self.coin_size = 20
        self.coin_count = 0

    def move_player(self, keys):
        if keys[pygame.K_LEFT]:
            self.player.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.player.x += self.speed

    def spawn_coins(self):
        if random.randint(1, 50) == 1:
            coin = pygame.Rect(random.randint(0, self.WIDTH - self.coin_size), 0, self.coin_size, self.coin_size)
            self.coins.append(coin)

    def update_coins(self):
        for coin in self.coins[:]:
            coin.y += 5

            if self.player.colliderect(coin):
                self.coins.remove(coin)
                self.coin_count += 1
            elif coin.y > self.HEIGHT:
                self.coins.remove(coin)

    def draw(self, screen, font):
        screen.fill((50, 50, 50))

        pygame.draw.rect(screen, (0, 255, 0), self.player)

        for coin in self.coins:
            pygame.draw.rect(screen, (255, 255, 0), coin)

        text = font.render(f"Coins: {self.coin_count}", True, (255, 255, 255))
        screen.blit(text, (250, 10))