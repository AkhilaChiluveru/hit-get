import pygame, sys
from random import randint
from Player import Player
from Targets import Targets 


pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Hit-Get')
clock=pygame.time.Clock() #to fix framerate

#background 
bg_surf=pygame.image.load('../graphics/background.png').convert()

#importing text
font=pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Hit-Get', True, (255,255,255))
text_rect= text_surf.get_rect(midbottom=(window_width/2,window_height-80))


#groups
player_group=pygame.sprite.Group()
bullet_group=pygame.sprite.Group()
targets_group=pygame.sprite.Group()

#object creation
player=Player(player_group)
target=Targets((100,300),targets_group)

#timer
target_timer=pygame.event.custom_type()
pygame.time.set_timer(target_timer,400)

while(True):
    #input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==target_timer:
            target_y_pos = randint(-150, -50)
            target_x_pos=randint(-100, window_width+100)
            Targets((target_x_pos,target_y_pos), groups=targets_group)

    #frame rate. 
    dt=clock.tick()/1000

    #background
    display_surface.blit(bg_surf,(0,0))

    #updates
    player_group.update(bullet_group)
    bullet_group.update(dt)
    display_surface.blit(text_surf,text_rect)
    targets_group.update(dt)

    #graphics on to the screen
    player_group.draw(display_surface)
    bullet_group.draw(display_surface)
    targets_group.draw(display_surface)


    #displaying frames to user
    pygame.display.update()

   
