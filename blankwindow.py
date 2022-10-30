
import pygame, sys
pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))

#setting the screen title
pygame.display.set_caption('Hit-Get')
clock=pygame.time.Clock() #to fix framerate

#importing images 
ship_surf = pygame.image.load('hit-get/graphics/ship.png').convert_alpha()

#x is constant as player moves slowly to the top.
ship_y_pos=500  

#importing background
bg_surf=pygame.image.load('hit-get/graphics/background.png').convert_alpha()

#importing text
font=pygame.font.Font('hit-get/graphics/subatomic.ttf', 50)
text_surf = font.render('Hit-Get', True, (255,255,255))

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
	ship_y_pos-=1
	display_surface.blit(ship_surf,(300,ship_y_pos))
	display_surface.blit(text_surf,(500,200))
	

	#showing the frame to the user
	pygame.display.update()
