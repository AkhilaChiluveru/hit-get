import pygame, sys
pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((window_width,window_height))

#setting the screen title
pygame.display.set_caption('Hit-Get')

#importing images
ship_surf = pygame.image.load('C:/Fall 2022/SE/hit-get/graphics/ship.png').convert_alpha()
#importing background
bg_surf=pygame.image.load('C:/Fall 2022/SE/hit-get/graphics/background.png').convert_alpha()
#importing text
font=pygame.font.Font('C:/Fall 2022/SE/hit-get/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))



while True: #to keep our game running
	#input
	for event in pygame.event.get():
		if event.type==pygame.QUIT: #the cross button on top of the screen to close the window
		   pygame.quit()
		   sys.exit()
	#updates
	display_surface.fill((0,0,0))
	display_surface.blit(bg_surf,(0,0))
	display_surface.blit(ship_surf,(300,500))
	display_surface.blit(text_surf,(500,200))
	

	#showing the frame to the user
	pygame.display.update()



