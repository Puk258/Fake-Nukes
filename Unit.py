import pygame
from Sprite_Sheet_Functions import *
from PIL import Image

class Units(pygame.sprite.DirtySprite):
    """
    Unit object, uses stats to add attributes. Stats are defined in Constants.py.
    """
    def __init__(self, stats):
        pygame.sprite.DirtySprite.__init__(self)
        self.move_sprite_list = []
        self.fire_sprite_list = []
        self.current_frames = []
        self.health = stats[0]
        self.move_filename = stats[1]
        self.fire_filename = stats[7]
        self.speed = stats[3]
        self.attack = stats[4]
        self.cost = stats[5]
        self.index = stats[6]
    
        """
        Uses SpriteSheetFunctions.py to load sprite sheets and cut them into
        single frames. Unit object has two sprite sheets, one for movement and
        one for attack. x and y define the size of the entire sprite sheet file,
        xf and yf define the bounderies of each image.
        """
        sprite_sheet = SpriteSheet(self.move_filename)
        with Image.open(self.move_filename) as img:
            x, y = img.size
            if x < y:
                xf, yf = 1, 20
            else: xf, yf = 4, 5

        x, y = (x/xf), (y/yf)

        for i in range(yf):
            for s in range(xf):
                image = sprite_sheet.get_image((x*s), (y*i), x, y)
                self.move_sprite_list.append(image)

        sprite_sheet = SpriteSheet(self.fire_filename)
        with Image.open(self.fire_filename) as img:
            x, y = img.size
        x, y = (x/xf), (y/yf)
        for i in range(yf):
            for s in range(xf):
                image = sprite_sheet.get_image((x*s), (y*i), x, y)
                self.fire_sprite_list.append(image)

        self.image = self.move_sprite_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = stats[2][0]
        self.rect.y = stats[2][1]
        self.frame = 0
        self.current_frames = self.move_sprite_list

    def update(self):
        """
        determines the current image to be displayed as well as its position, if
        the last image in the list, resets to 0.
        """
        self.dirty = 2
        x = (len(self.current_frames) - 1)
        if self.frame == (x):
            self.frame = 0
            self.image = self.current_frames[self.frame]
            changex = self.speed[0]
            changey = self.speed[1]
            self.rect.x += changex
            self.rect.y += changey
        else:
            self.frame += 1
            self.image = self.current_frames[self.frame]
            changex = self.speed[0]
            changey = self.speed[1]
            self.rect.x += changex
            self.rect.y += changey
