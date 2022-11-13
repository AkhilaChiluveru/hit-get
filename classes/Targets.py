import pygame
from random  import uniform,randint

class Targets(pygame.sprite.Sprite):
    def __init__(self,positon,groups):
        super().__init__(groups)
        self.image=pygame.image.load('../graphics/targets.png').convert_alpha()
        self.rect=self.image.get_rect(center=positon)

        self.pos=pygame.math.Vector2(self.rect.topleft)
        self.direction=pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed=randint(400,600)
    def update(self,dt):
        self.pos+=self.direction * self.speed * dt
        self.rect.topleft=(round(self.pos.x),round(self.pos.y))



       