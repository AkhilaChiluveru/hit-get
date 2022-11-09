import pygame
window_width,window_height=1280,720
class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect=self.image.get_rect(center=(window_width/2,window_height/2))