import random, pygame
from pygame import *
#from AoWFun3 import *
from Unit import *
import Background
from Constants import *
from Background import *
from math import *


Firework = [0,"Sprites/Firework.png",[683,600],[1,-5],0,0,"Firework","Sprites/Firework.png"]
Sparkle = [0,"Sprites/Sparkle.png",[683,600],[1,-5],0,0,"Sparkle","Sprites/Sparkle.png"]
party = sprite.Group()
class GravitySprite(Units): # Create new sprite to be used for the Fireworks that will act as if under gravity
    def __init__(self, stats,vector,speed):
        super().__init__(stats)
        self.counter1 = stats[4]
        self.counter2 = stats[5]
        self.speed = speed
        self.vector = vector
        self.dy = 0
        self.angle = 0

    def update(self):
        super().update()
        #Change the vertial speed gradually over time to simulate gravity. This is done by running over a list of speeds so that the object
        #doesn't move vertically by the same number of pixels each tick
        if self.counter1 == len(self.vector): #If counter 1 goes out of range, set it back to zero, increase one of the speeds in the list and increment up counter 2.
                self.counter1 = 0
                self.vector[self.counter2] += 1
                self.counter2 += 1
                if self.counter2 == len(self.vector):   #If counter 2 gous out of range set it back to zero
                    self.counter2 = 0
        self.speed[1] = self.vector[self.counter1] # Set the vertical speed of the object to the next speed in the list and increment counter 1.
        self.counter1 +=1

        #Rotation of the image to simulate gravity
        for v in self.vector: #Average the speeds in the vector list for a more smooth transition
            self.dy += v
        self.dy = self.dy/len(self.vector)

        try: # Set the angle of the ratation dependent on the average of the speeds. For the one tick where dividing by zero occurs, don't change the rotation
            self.angle = atan(self.speed[0]/self.dy)
        except ZeroDivisionError:
            pass
        if self.angle > 0 and self.speed[0] >0 or self.angle < 0 and self.speed[0] <0:
            self.angle = -3.142 + self.angle
        self.image = transform.rotate(self.image,self.angle*57.298)
            
        
              
pygame.init()
clock = time.Clock()
time.set_timer(11,1200)
def WinScreen(Message):
 battlefield = Background.battlefield(game)#Set the background image to be the game background.
 dx = 3
 while True:
        battlefield.draw(screen)
        events =  event.poll()
        if events.type == KEYDOWN and events.key == K_ESCAPE or events.type == QUIT: #Quit the game on escape or Quit
            break
        
        if events.type == 11: #every time the timer pings, spawn a new firework pointing in the opposite direction to the previous firework.
            party.add(GravitySprite(Firework,[-11,-11,-11],[dx,-5]))
            dx = -dx
            


        for unit in party:
            unit.update()#Move the firework
            if unit.index == "Firework": # For the firework rockets, if a certain downwards speed is reached, kill the sprite and spawn a random set of Sparkles
                if unit.speed[1] > 4:
                    ddx = -1
                    while ddx <= 2:
                        ddx += (random.randrange(-2,2))/10
                        y = -1
                        while y <= 2:
                            y += (random.randrange(-2,2))/10
                            Fire = GravitySprite(Sparkle,[y,y,y],[ddx,-5])
                            Fire.rect.x = unit.rect.x
                            Fire.rect.y = unit.rect.y
                            party.add(Fire)
                            y+=1
                        ddx+=1
                    unit.kill()
            if unit.index == "Sparkle": #If the Sparkle goes off the edge of the screen, remove it to improve framerate.
                if unit.rect.y > 705:
                    unit.kill()
                    
                    
        WinMessage = Font.render(Message, True, WHITE)
        
        pygame.draw.rect(screen,BROWN,(620,10,200,80))
        pygame.draw.rect(screen,BLACK,(630,20,180,60))
        screen.blit(WinMessage,(650,40))
        party.draw(screen)
        display.flip()
        time.delay(30)
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


#WinScreen("Player 1 Wins!")

