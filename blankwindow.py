
import pygame, sys
pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))

#setting the screen title
pygame.display.set_caption('Hit-Get')
clock=pygame.time.Clock() #to fix framerate

#importing images 
ship_surf = pygame.image.load('./graphics/player.png').convert_alpha()
bg_surf=pygame.image.load('./graphics/background.png').convert()

#importing text
font=pygame.font.Font('graphics/subatomic.ttf', 50)
text_surf = font.render('Hit-Get', True, (255,255,255))

#movements
ship_rect=ship_surf.get_rect(center=(window_width/2,window_height/2))  
text_rect= text_surf.get_rect(midbottom=(window_width/2,window_height-80))

while True:
	#input
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		
	#To set framerate, speed doesnt depend on while loop
	clock.tick(60) 
	
	#mouse inputs to handle player
	ship_rect.center= pygame.mouse.get_pos()
 
	#updates
	display_surface.fill((0,0,0))
	display_surface.blit(bg_surf,(0,0))
	display_surface.blit(ship_surf,ship_rect)
	display_surface.blit(text_surf,text_rect)
	
	#showing the frame to the user
	pygame.display.update()

