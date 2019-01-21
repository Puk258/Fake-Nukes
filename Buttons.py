import pygame
from pygame import *

pygame.init()
screen = pygame.display.set_mode((1366,705))
menuButtonFont = pygame.font.SysFont("calibri", 25)
spawnButtonFont = pygame.font.SysFont("calibri",15)

white = (255,255,255)
grey = (150,150,150)
lightgrey = (50,50,50)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
brown = (100,0,0)

#button base class
class Button():

    def __init__(self, xpos, ypos, width, height, color, hovercolor):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.hovercolor = hovercolor

    #if the mouse position is above the button, trigger a hover flag
    def hover(self):
        mouse = pygame.mouse.get_pos()
        if self.xpos+self.width>mouse[0]>self.xpos and self.ypos+self.height>mouse[1]>self.ypos:
            return True
        else:
            return False

    #draw method to create the rect object 
    def draw(self):
        pygame.draw.rect(screen, self.color,(self.xpos,
                                                 self.ypos,
                                                 self.width,
                                                 self.height))
        self.onClick()

    #uses the hover method. If it returns true and you click on it then return True
    def onClick(self):
        click = pygame.mouse.get_pressed()
        if self.hover() and click[0] == 1:
            return True
        else:
            return False

#special type of button designed for Menu. 
class MenuButton(Button):

    #extra things defined are text and cost
    def __init__(self,text, xpos, ypos, width, height, color, hovercolor, cost = 0):
        self.text = menuButtonFont.render(text, False, green)
        self.cost = 0 
        if cost != 0:
            self.cost = spawnButtonFont.render(str("Cost: {}".format(cost)), False, green)
        super().__init__(xpos, ypos, width, height, color, hovercolor)

    #Draw this and blit it to the screen. If no cost is defined then dont include that. 
    def draw(self):
        super().draw()
        if super().hover():
            pygame.draw.rect(screen, self.hovercolor,(self.xpos,
                                                 self.ypos,
                                                 self.width,
                                                 self.height))
        #center the text in the rectangle
        screen.blit(self.text,(((self.xpos+self.xpos+self.width)/2)-(self.text.get_width()/2),((self.ypos+self.ypos+self.height)/2)-(self.text.get_height()/2)))
        if self.cost != 0:
            screen.blit(self.cost,(((self.xpos+self.xpos+self.width)/2)-(self.text.get_width()/2),((self.ypos+self.ypos+self.height)/2)+ self.text.get_height() -(self.text.get_height()/2) - 6))


#spawnbutton that has an image associated with it. Hovering over it also renders more information 
class SpawnButton(Button):

    #Extra things when you hover over it have been defined.
    def __init__(self, text, xpos, ypos, width, height, color, hovercolor, image, health, speed, attack,cost, strongAgainst = "Foot", weakAgainst = "Tank"):
        self.text = spawnButtonFont.render(text + " : " + str(cost), False, green)
        self.health = spawnButtonFont.render("Health: " + str(health), False, green)
        self.speed = spawnButtonFont.render("Speed: " + str(speed), False, green)
        self.attack = spawnButtonFont.render("Attack: " + str(attack), False, green)
        self.strongAgainst = spawnButtonFont.render("Strong: " + strongAgainst, False, green)
        self.weakAgainst = spawnButtonFont.render("Weak: " + weakAgainst, False, green)
        self.image = image
        super().__init__(xpos, ypos, width, height, color, hovercolor)

    def draw(self):
        super().draw()

        #center the image in the rect
        screen.blit(self.image,(((self.xpos+self.xpos+self.width)/2)-(self.image.get_width()/2),((self.ypos+self.ypos+self.height)/2)-(self.image.get_height()/2)))

        #if hovering over it add all these texts
        if super().hover():
            pygame.draw.rect(screen, self.hovercolor,(self.xpos,
                                                 self.ypos,
                                                 self.width,
                                                 self.height))
            #text for stats here. position relative to the font...
            screen.blit(self.health,(self.xpos+1,self.ypos+1+self.text.get_height()))
            screen.blit(self.attack,(self.xpos+1,self.ypos+1+self.text.get_height()*2))
            screen.blit(self.strongAgainst,(self.xpos+1,self.ypos+1+self.text.get_height()*3))
            screen.blit(self.weakAgainst,(self.xpos+1,self.ypos+1+self.text.get_height()*4))
        #placement of text
        screen.blit(self.text,(self.xpos+1,self.ypos+1))
