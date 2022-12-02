import unittest
import pygame
from Targets import Targets
display_surface=pygame.display.set_mode((1280,720))
window_width,window_height=1280,720

class Targets_test(unittest.TestCase):
        pygame.init()

        def test_init(self): 
            target_group=pygame.sprite.Group()
            pos=pygame.mouse.get_pos()
            targets=Targets(pos,target_group)
            self.assertEqual(type(Targets(pos,pygame.sprite.Group())),type(targets))
        def pygame_modules_have_loaded():
                if not pygame.image.get_init:
                        success=False
                if not pygame.math.get_int:
                        success=False
                return success

if __name__=='__main__':
        unittest.main()