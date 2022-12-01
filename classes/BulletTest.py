import unittest
import pygame
from Bullet import Bullet
import Score
from unittest.mock import patch
display_surface=pygame.display.set_mode((1280,720))
window_width,window_height=1280,720

class Bullet_test(unittest.TestCase):
    pygame.init()

    def test_init(self):
        bullet_group= pygame.sprite.Group()
        pos=pygame.mouse.get_pos()
        bullet = Bullet(pos,bullet_group)
        self.assertEqual(type(Bullet(pos,pygame.sprite.Group())), type(bullet))

    @patch('pygame.sprite.spritecollide')
    def test_score_increment_onCollision(self,mock_sprite_collision):
        mock_sprite_collision.return_value= True
        target_group=pygame.sprite.Group()
        bullet_group= pygame.sprite.Group()
        pos=pygame.mouse.get_pos()
        bullet = Bullet(pos,bullet_group)
        Score.varScore=5
        prev_score=5
        bullet.hit_target(target_group)
        self.assertEqual(prev_score+1, Score.varScore)

    @patch('pygame.sprite.spritecollide')
    def test_score_increment_onNoCollision(self,mock_sprite_collision):
        mock_sprite_collision.return_value= False
        target_group=pygame.sprite.Group()
        bullet_group= pygame.sprite.Group()
        pos=pygame.mouse.get_pos()
        bullet = Bullet(pos,bullet_group)
        Score.varScore=5
        prev_score=5
        bullet.hit_target(target_group)
        self.assertEqual(prev_score, Score.varScore)

if __name__=='__main__':
        unittest.main()