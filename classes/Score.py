import pygame


class Score():

	def __init__(self):
		self.font = pygame.font.Font('./graphics/subatomic.ttf',30)
		global varScore
		varScore=0

	def display(self,display_surface,WINDOW_WIDTH,WINDOW_HEIGHT):
		score_text = f'Score: {varScore} Timer: {pygame.time.get_ticks()//1000}'
		text_surf = self.font.render(score_text,True,(255,255,255))
		text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30))
		display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(
			display_surface, 
			(200,200,200),
			text_rect.inflate(30,30), 
			width = 1,
			border_radius = 3
		)

