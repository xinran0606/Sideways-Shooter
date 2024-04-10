import pygame

class Ship:

    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()
        self.image = pygame.image.load ('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)