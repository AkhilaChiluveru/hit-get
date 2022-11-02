import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,groups):
        super().__init__(groups)
        self.image=pygame.image.load('./graphics/laser.png').convert_alpha()
        self.rect=self.image.get_rect(midbottom=position)

