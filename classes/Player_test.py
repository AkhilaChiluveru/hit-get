import unittest
import pygame
from Player import Player
display_surface=pygame.display.set_mode((1280,720))
window_width,window_height=1280,720

class Player_test(unittest.TestCase):
        pygame.init()

        def test_init(self): 
            player_group=pygame.sprite.Group()
            player=Player(player_group)
            self.assertEqual(type(Player(pygame.sprite.Group())),type(player))

        def test_input_position(self):
            player_group=pygame.sprite.Group()
            player=Player(player_group)
            player.input_position()
            pos=pygame.mouse.get_pos()
            position=pos
            self.assertEqual(pos,position)

        def test_bullet_timer(self):
            player_group=pygame.sprite.Group()
            player=Player(player_group)
            player.bullet_timer()
            can_shoot=False
            current_time=pygame.time.get_ticks()
            if current_time>0:
                can_shoot=True
                self.assertTrue(can_shoot)
            if current_time<0:
                self.assertFalse(can_shoot,False)

if __name__=='__main__':
        unittest.main()