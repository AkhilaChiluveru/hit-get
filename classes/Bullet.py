import pygame
import Score
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,groups):
        super().__init__(groups)
        self.image=pygame.image.load('../graphics/bullets.png').convert_alpha()
        self.rect=self.image.get_rect(midbottom=position)

        self.pos=pygame.math.Vector2(self.rect.topleft)
        self.direction=pygame.math.Vector2(0,-1) #-1 for upwards 0 for left/ right
        self.speed=1000
        self.explosion_sound=pygame.mixer.Sound('../sounds/explosion.wav')
        
    def hit_target(self,target_group):
        if pygame.sprite.spritecollide(self,target_group,True):
            Score.varScore+=1
            self.kill()
            self.explosion_sound.play()

    def update(self,dt,target_group):
        self.pos += self.direction* self.speed * dt 
        self.rect.topleft= (round(self.pos.x),round(self.pos.y))

        if self.rect.bottom < 0:
            self.kill()
        
        self.hit_target(target_group)