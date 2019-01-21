import random
import pygame
from Functions import *
from Background import *

#created a list of images for the different parts of the tutorial page
spawnpage = pygame.image.load("Sprites/spawnpage.png")
powerpage = pygame.image.load("Sprites/powerpage.png")
upgradepage = pygame.image.load("Sprites/upgradepage.png")
buttonpage = pygame.image.load("Sprites/buttonpage.png")
backgrounds = [spawnpage,powerpage,upgradepage,buttonpage]


#method is called when the user selects tutorial in the start menu
def SpawnPage():
    Next = MenuButton("Next",550,243,255,50,brown,lightgrey)
    Previous = MenuButton("Previous",550,303,255,50,brown,lightgrey)
    MainMenu = MenuButton("Main Menu",550,183,255,50,brown,lightgrey)
    
    counterump = 0
    while True:

    #if statements are used to selectively draw the buttons only when they're required 
        keypress =  event.poll()
        screen.blit(backgrounds[counterump],(0,0))
        if counterump < 3:
            Next.draw()
        if counterump > 0:
            Previous.draw()
        

        if Next.onClick():
            #increment the index of the background list from the image.
            counterump+=1
            time.delay(300)

        if Previous.onClick():
            counterump-=1
            time.delay(300)

        MainMenu.draw()

        #break out of the loop if required. 
        if MainMenu.onClick():
            break
        
        
        
        display.flip()

