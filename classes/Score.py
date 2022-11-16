import pygame


class Score():

	def __init__(self):
		self.font = pygame.font.Font('./graphics/subatomic.ttf',50)

	def display(self,display_surface,WINDOW_WIDTH,WINDOW_HEIGHT,scoreCount):
		# exercise: recreate the original display_score function inside of a class
		# actually call it in the game loop
		score_text = f'Score: {pygame.time.get_ticks() // 100}'
		text_surf = self.font.render(score_text,True,(255,255,255))
		text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30))
		display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(
			display_surface, 
			(200,200,200),
			text_rect.inflate(40,40), 
			width = 2,
			border_radius = 5
		)

