import pygame, sys
from Bullet import Bullet

window_width,window_height=1280,720

class Player(pygame.sprite.Sprite):
    
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect=self.image.get_rect(center=(window_width/2,window_height/2))
        self.can_shoot = True
        self.shoot_time= None

    def bullet_timer(self):
        if not self.can_shoot:
            current_time=pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot =True

    def input_position(self):
        pos=pygame.mouse.get_pos()
        self.rect.center=pos

    def bullet_shoot(self,bullet_group):
        # If left button is pressed for a little longer time or long pressed, it would create sequence of bullets. With can_shoot variable and shoot_time we control that
        #left button in mouse
       if pygame.mouse.get_pressed()[0] and self.can_shoot:
           self.can_shoot = False
           self.shoot_time=pygame.time.get_ticks()
           Bullet(self.rect.midtop,bullet_group)

    def hit_target(self,target_group):
        if pygame.sprite.spritecollide(self,target_group,False):
            pygame.quit()
            sys.exit()

    def update(self,bullet_group,target_group):
        self.bullet_timer()
        self.bullet_shoot(bullet_group)
        self.input_position()
        self.hit_target(target_group)
        