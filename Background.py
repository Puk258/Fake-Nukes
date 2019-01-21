import pygame
import Constants

game = pygame.image.load("Sprites/backgrounds/BackgroundMain.png").convert()
menu = pygame.image.load("Sprites/backgrounds/MenuBackground1.png").convert()
class battlefield():
    def __init__(self,background):
        self.background = background#self.background.set_colorkey(Constants.WHITE)
        self.units = None
        self.enemyunits = None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(Constants.WHITE)
        screen.blit(self.background, [0, 0])
