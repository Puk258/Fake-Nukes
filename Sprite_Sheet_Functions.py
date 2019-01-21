from pygame import *
from Constants import *

class SpriteSheet(pygame.sprite.DirtySprite):
    """
    Loads the spritesheet, removes the background colour, and copies it to the
    smaller image which is returned.
    """
    def __init__(self, fileName):
        self.sprite_sheet = pygame.image.load(fileName).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image
