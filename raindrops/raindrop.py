import pygame
from pygame.sprite import Sprite
class Raindrop(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/raindrop.bmp')
        self.drop_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.drop_rect.top = self.screen_rect.top - self.drop_rect.height
        self.drop_rect.left = self.screen_rect.left + self.drop_rect.width
    def update(self):
        if self.drop_rect.y < self.screen_rect.bottom:
            self.drop_rect.y += 1

    def blit_me(self):
        self.screen.blit(self.image,self.drop_rect)