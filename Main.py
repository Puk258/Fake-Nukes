""" Build a start screen menu for the Game where you can choose difficulty(How money the AI
    starts with and makes over time,
    and then it comes up with a countdown until the game starts and you can start
    spawning"""

""" Add more SOUND"""

""" More fully implement Two player, show on screen the evil money and maybe instead of the
    amran buttons for two player show the hotkeys for each player?"""

""" Add Tech Trees"""

""" add overlays for the buttons so that when you hover over something like Inf it will
    show you their cost damage stats ect in a larger box and a picture of the unit rather
    than current change of colour."""

""" maybe put some functions in the main while loop into if statements so that they don't
    run every tick but only certain ones to increase speed of game??"""

""" Create tutorial especially for two play explaing the hotkeys"""

""" Add single player Helicopter mode"""

''' spawn delay '''
''' animations '''
''' sound '''



import random
from pygame import *
from Functions import *
from Start_Menu import *
import Sprite_Sheet_Functions
import Unit
import Background
from Win_Screen import *
from Actions import *
from Constants import *
from Buttons import*
from AI_File import *

#Initialises all of the powers classes
extras = sprite.Group()
extras.add(Airstrike())
extras.add(Assassinate())
extras.add(Immortality())
ML = Mlevel()
HL = Hlevel()
AL = Alevel()
extras.add(ML,HL,AL)
extras.add(Inf())
extras.add(Tank())
extras.add(Rocket())

def main():
 Quit = False
 pygame.init()
 clock = time.Clock()
 time.set_timer(11,300)
 Quit = StartMenu(Quit)
 size = [Constants.SCREENWIDTH, Constants.SCREENHEIGHT]
 screen = pygame.display.set_mode(size)
 pygame.display.set_caption("Fake Nukes")
 battlefield = Background.battlefield(game)
 while True:
        events =  event.poll()
        #For both armies, check to see if out of health, if out of health, remove from the P1.army
        P2.money = ClearDead(P1.army,P2.money,ML.P2level)
        P1.money = ClearDead(P2.army,P1.money,ML.P1level)
        P1.spawnpos = CheckSpawn(P1.army)
        P2.spawnpos = CheckSpawn(P2.army)

        #Quits if Quit buttons pressed or if Quit is set to true in  menu
        if events.type == QUIT or Quit == True:
            break
        if events.type == KEYDOWN and events.key == K_ESCAPE:
            Quit = StartMenu(Quit)
            
        MoveAttack(P1.army,P2.army,AL.P1level,HL.P2level)
        MoveAttack(P2.army,P1.army,AL.P2level,HL.P1level)

        battlefield.draw(screen)
        AI()
        #Runs the check file for all of the powers
        for e in extras:
                e.check(events,screen)

        if not P2.AIToggle:
            void1.draw()
            void2.draw()
            void3.draw()

        #code to render the text onto the screen
        moneyLeft = Font.render("Player 1 Money:" + str(int(P1.money)), True, (255, 255, 255))
        screen.blit(moneyLeft,(10,530))
        if not P2.AIToggle:
            EmoneyLeft = Font.render("Player 2 Money:" + str(int(P2.money)), True, (255, 255, 255))
            screen.blit(EmoneyLeft,(983,530))

        #error statements for not enough money and spawn position not possitble
        if events.type == KEYDOWN and P1.spawnpos == False:
            pass
        elif events.type == KEYDOWN: # If you dont have enough money print this message
            pass

        #increment money
        P1.money += 0.1
        P2.money += 0.1*P1.Diff

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #This is what happens if the player1 wins the game 
        for unit in P1.army:
            if unit.index != "P1Plane" and unit.rect.x > 1355:
                    WinScreen("Player 1 Wins!")
                    Quit = True
                    break
            unit.update()
        #what happens if player 2 wins the game
        for unit in P2.army:
            if unit.index != "P2Plane" and unit.rect.x < 11:
                    WinScreen("Player 2 Wins!")
                    Quit = True
                    break
            unit.update()
        P1.army.draw(screen)
        P2.army.draw(screen)
        display.update()
        clock.tick(20)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))
 pygame.quit()
main()
