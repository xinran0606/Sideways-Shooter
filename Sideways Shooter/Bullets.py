import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.image = pygame.image.load('images/bullet.bmp')
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.midleft = ss_game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self):
         self.x -= self.settings.bullet_speed
         self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)