import pygame, sys
from Player import Player
from Bullet import Bullet 
from Targets import Targets 


pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Hit-Get')
clock=pygame.time.Clock() #to fix framerate

#background 
bg_surf=pygame.image.load('./graphics/background.png').convert()

#groups
player_group=pygame.sprite.Group()
bullet_group=pygame.sprite.Group()
targets_group=pygame.sprite.Group()

#object creation
player=Player(player_group)
bullet=Bullet((100,300),bullet_group)
target=Targets((100,300),targets_group)

while(True):
    #input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    #frame rate. 
    dt=clock.tick()/1000
    
    #Player movements
    player.rect.center=pygame.mouse.get_pos()

    #background
    display_surface.blit(bg_surf,(0,0))

    #graphics on to the screen
    player_group.draw(display_surface)
    bullet_group.draw(display_surface)
    targets_group.draw(display_surface)

    #displaying frames to user
    pygame.display.update()

   
