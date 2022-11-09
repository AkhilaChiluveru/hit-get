import pygame

class Targets(pygame.sprite.Sprite):
    def __init__(self,positon,groups):
        super().__init__(groups)
        self.image=pygame.image.load('./graphics/targets.png').convert_alpha()
        self.rect=self.image.get_rect(center=positon)
       