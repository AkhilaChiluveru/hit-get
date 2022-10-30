
import pygame, sys
pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))

#setting the screen title
pygame.display.set_caption('Hit-Get')
clock=pygame.time.Clock() #to fix framerate

#importing images 
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()

ship_rect=ship_surf.get_rect(center=(window_width/2,window_height/2))  

#importing background
bg_surf=pygame.image.load('./graphics/background.png').convert_alpha()

#importing text
font=pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Hit-Get', True, (255,255,255))
text_rect= text_surf.get_rect(midbottom=(window_width/2,window_height-80))
while True: #to keep our game running
	#input
	for event in pygame.event.get():
		if event.type==pygame.QUIT: #the cross button on top of the screen to close the window
			pygame.quit()
			sys.exit()
    #To set framerate
	clock.tick(60) #speed doesnt depend on while loop
	#updates
	display_surface.fill((0,0,0))
	display_surface.blit(bg_surf,(0,0))
	if ship_rect.top > 0:
		ship_rect.y-=4
	display_surface.blit(ship_surf,ship_rect)
	display_surface.blit(text_surf,text_rect)
	

	#showing the frame to the user
	pygame.display.update()
