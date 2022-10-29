import pygame, sys
pygame.init()
window_width,window_height=1280,720
display_surface=pygame.display.set_mode((screen_width,screen_height))
#setting the screen title
pygame.display.set_caption('Hit-Get')

while True: #to keep our game running
	#input
	for event in pygame.event.get():
		if event.type==pygame.QUIT: #the cross button on top of the screen to close the window
		   pygame.quit()
		   sys.exit()
	#showing the frame to the user
	pygame.display.update()



