import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,groups):
        super().__init__(groups)
        self.image=pygame.image.load('./graphics/bullets.png').convert_alpha()
        self.rect=self.image.get_rect(midbottom=position)

        self.pos=pygame.math.Vector2(self.rect.topleft)
        self.direction=pygame.math.Vector2(0,-1) #-1 for upwards 0 for left/ right
        self.speed=600

    def update(self,dt):
        self.pos += self.direction* self.speed * dt 
        self.rect.topleft= (round(self.pos.x),round(self.pos.y))