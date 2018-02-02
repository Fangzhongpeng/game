import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
        """表示单个外星人的类"""
        def __init__(self,ai_settings,screen):
               super(Alien, self).__init__()
               self.screen = screen
               self.ai_settings = ai_settings
               self.image = pygame.image.load('images/test.ico')
               self.rect = self.image.get_rect()
               self.rect.x = self.rect.width
               self.rect.y = self.rect.height
               self.x = float(self.rect.x)
        def blitme(self):
                self.screen.blit(self.image,self.rect)