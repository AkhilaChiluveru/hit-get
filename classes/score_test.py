import unittest
import pygame
from Score import Score
display_surface=pygame.display.set_mode((1280,720))
window_width,window_height=1280,720

class Score_test(unittest.TestCase):
        pygame.init()

        def test_init(self): 
            score=Score()
            self.assertEqual(type(Score()),type(score))

        def test_display(self):
            varScore=5
            score=Score()
            score.display(display_surface,window_width,window_height) 
            score_text = f'Score: {varScore} Timer: {pygame.time.get_ticks()//1000}'
            test_score_text= f'Score: 5 Timer: {pygame.time.get_ticks()//1000}'
            self.assertEqual(score_text,test_score_text)


if __name__=='__main__':
        unittest.main()