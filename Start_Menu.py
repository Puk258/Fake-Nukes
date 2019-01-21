import random
from pygame import *
from Functions import *
from Background import *
from Constants import *
from Tutorial import *


def StartMenu(Quit):
    if P1.start: #If it is the first time that you open the menu, there should be no resume button
        pos = 50
    else:
        pos = 0

    #Setup the buttons for the first menu screen
    buttons = []
    Resume = MenuButton("Resume",511,223,255,50,brown,lightgrey)
    SPlay = MenuButton("Single Player",511,273-pos,255,50,brown,lightgrey)
    TPlay = MenuButton("Two Player",511,323-pos,255,50,brown,lightgrey)
    Exiteru = MenuButton("Exit",511,423-pos,255,50,brown,lightgrey)
    Tutorial = MenuButton("Tutorial",511,373-pos,255,50,brown,lightgrey)

    if not P1.start: #If its not the first time opening the game, add resume to the group to be drawn
        buttons.append(Resume)
        pygame.mixer.Channel(3).pause()
        pygame.mixer.Channel(2).unpause()
    if P1.start:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("Sounds&Music/Charge.wav"))
        pygame.mixer.Channel(2).set_volume(0.2)
    buttons.append(SPlay)
    buttons.append(TPlay)
    buttons.append(Tutorial)
    buttons.append(Exiteru)

    #Set the background to the menu screen
    startfield = battlefield(menu)

    while True:
        #Draw the background and the different buttons on the screen
        startfield.draw(screen)
        keypress =  event.poll()
        for button in buttons:
            button.draw()

        if SPlay.onClick(): #If single player turn on the AI and start the single player menu
            time.delay(200)
            P2.AIToggle = True
            SingleMenu(Quit)
            break
        if Tutorial.onClick():
            SpawnPage()
        if TPlay.onClick():
            pygame.mixer.Channel(2).pause() #If two player pause the music, turn off the AI, set difficulty to one and start the game.
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sounds&Music/BackgroundFight.wav"))
            P2.AIToggle = False
            P1.Diff = 1
            P1.money,P2.money = 500, 500
            P1.start = False
            P1.army,P2.army = sprite.Group(),sprite.Group()
            break
        if keypress.type == KEYDOWN and keypress.key == K_ESCAPE or Resume.onClick(): #If escape or resume pressed, then restart the game
            pygame.mixer.Channel(2).pause()
            pygame.mixer.Channel(3).unpause()
            break
        if Exiteru.onClick() or keypress.type == QUIT: # If Quit is pressed, exit the game
            Quit = True
            return Quit
        display.flip()


    return Quit
def SingleMenu(Quit):
    EPlay = MenuButton("Easy",511,223,255,50,brown,lightgrey)
    MPlay = MenuButton("Medium",511,273,255,50,brown,lightgrey)
    HPlay = MenuButton("Hard",511,323,255,50,brown,lightgrey)
    Back = MenuButton("Back",511,373,255,50,brown,lightgrey)
    while True:
            keypress =  event.poll()
            EPlay.draw()
            MPlay.draw()
            HPlay.draw()
            Back.draw()
            #Set the different difficulty levels up for the AI depending on which button is clicked and pause the music
            if EPlay.onClick():
                pygame.mixer.Channel(2).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sounds&Music/BackgroundFight.wav"))
                P1.Diff = 1
                P1.money,P2.money = 1500,1500
                P1.army,P2.army = sprite.Group(),sprite.Group()
                break
            if MPlay.onClick():
                pygame.mixer.Channel(2).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sounds&Music/BackgroundFight.wav"))
                P1.Diff = 2
                P1.money,P2.money = 1000,1500
                P1.army,P2.army = sprite.Group(),sprite.Group()
                break
            if HPlay.onClick():
                pygame.mixer.Channel(2).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sounds&Music/BackgroundFight.wav"))
                P1.Diff = 3
                P1.money,P2.money = 500,1500
                P1.army,P2.army = sprite.Group(),sprite.Group()
                break

            if Back.onClick(): #If the back button is pressed, used recursion to call the first start menue again.
                time.delay(200)
                StartMenu(Quit)
                break
            display.flip()
    P1.start = False
    return Quit

#Quit = StartMenu(Quit)
if __name__ == '__StartMenu__':
    StartMenu()
