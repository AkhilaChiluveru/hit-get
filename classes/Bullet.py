import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,groups):
        super().__init__(groups)
        self.image=pygame.image.load('./graphics/bullets.png').convert_alpha()
        self.rect=self.image.get_rect(midbottom=position)

