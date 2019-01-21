import random
from pygame import *
from Buttons import *
from Unit import *
from Constants import *
#Initialises the classes used for the actions using the format shown below
#stats = [button,cost,key1,key2,identifier(ONLY USED FOR UPGRADES,P1level,P2,level)]
airstrike = [strikebutton,P1Plane[5],K_q, K_u,4]
assassinate = [killbutton,killmoney,K_w,K_i,4]
immortality = [immortalbutton,immortalmoney,K_e,K_o,4]
mlevel = [Upmoneybutton,upmmoney,K_z,K_m,0,0,0]
hlevel = [Uphealthbutton,uphmoney,K_x,44,1,0,0]
alevel = [Upattackbutton,upamoney,K_c,46,2,0,0]
inf = [Infbutton,P1Inf[5],K_a,K_j,3]
tank = [Tankbutton,P1Tank[5],K_s,K_k,3]
rocket = [Rocketbutton,P1Rocket[5],K_d,K_l,3]
events = event.poll()

#A dictionary linking the key binding with the unit that needs to be spawned to be used in the class SpawnUnit
dic = {K_a:P1Inf, K_s:P1Tank, K_d:P1Rocket, K_j:P2Inf, K_k:P2Tank, K_l:P2Rocket}
        
class Actions (pygame.sprite.DirtySprite):
    def __init__(self,stats):
        pygame.sprite.DirtySprite.__init__(self) 
        self.button = stats[0]
        self.cost = stats[1]
        self.key1 = stats[2]
        self.key2 = stats[3]
        self.identifier = stats[4]

    def check(self,events,screen):
        self.button.draw()# Draw  the buttons of each action onto the screen
        #Check to see if a button has been pressed and whether the player has enough money for the relevant actions.
        if (P1.money >= self.cost and self.button.onClick()) or events.type == KEYDOWN and (events.key == self.key1 and P1.money >= self.cost or events.key == self.key2 and not P2.AIToggle and P2.money >= self.cost):
            if events.type == KEYDOWN and events.key == self.key2: #Checks to see which player pressed the button and that the action can be completed (Upgrades and spawning)
                if self.identifier < 3 and self.P2level > 4 or self.identifier == 3 and P2.spawnpos == False:
                    pass
                else:
                    time.delay(50)
                    P2.money -= self.cost   #Charges the player and runs the actions
                    self.action(P2Plane,P2.army,P1.army)
            else:
                if self.identifier < 3 and self.P1level > 4 or self.identifier == 3 and P1.spawnpos == False:
                    pass
                else:
                 time.delay(50)
                 P1.money -= self.cost
                 self.action(P1Plane,P1.army,P2.army)

        self.update(P1.army,events) #For both teams run the update function on each of the classes
        self.update(P2.army,events)
        
class Airstrike(Actions):
    def __init__(self):
        Actions.__init__(self,airstrike)

    def action(self,plane,army,Earmy):
        army.add(Units(plane)) #When the button is pressed, spawn a plane of the same team
        

    def update(self,army,events):
        for a in army: #When a plane reaches a point on the screen spawn a shell at that place and add it to the respective army
            if a.index == "P1Plane" or a.index =="P2Plane":
                if a.rect[0] == 216 or a.rect[0] == 660 or a.rect[0] == 1116 :    #This needs to be in multiples of 6
                    Shell[2] = [a.rect[0],50]
                    army.add(Units(Shell))
    
class Assassinate(Actions):
    def __init__(self):
        Actions.__init__(self,assassinate)

    def action(self,plane,army,Earmy): #Try and kill one random enemy unit, if they have no units do nothing
        try:
            blackspot = random.randrange(0,len(Earmy))
            Earmy.sprites()[blackspot].health = 0            
        except ValueError:
            pass

    def update(self,army,events): #No update function for this class is used but will be called in action so a pass is required
        pass

class Immortality(Actions):
    def __init__(self):
        Actions.__init__(self,immortality)


    def action(self,plane,army,Earmy): #Dependent on which player pressed the button (found using plane) set the respective immortalcount to zero
        if plane == P2Plane:
            P2.immortalcount = 0
        else:
            P1.immortalcount = 0
        

    def update(self,army,events):
        for p in Players: #If the immortal count is below zero set the heal of the players units to 100 
            if p.immortalcount < 5:
                for unit in p.army:
                    unit.health = 100
                if events.type == 11: #everytime the time pings, increment the immortal count.
                    p.immortalcount += 1

                if p == P1:  #For each of the players, display how long the immortality has left 
                    pos = 0
                else:
                    pos = 1166
                pygame.draw.rect(screen,BROWN,(pos,0,200,80))
                pygame.draw.rect(screen,BLACK,(pos+10,10,180,60))
                text = Font.render("Medics: " + str(5-p.immortalcount), True,WHITE)
                screen.blit(text,(pos+30,30))


class Upgrade(Actions):
    def __init__(self,upgrade):
        Actions.__init__(self,upgrade) 
        self.P1level = upgrade[5]#Each player will have their own upgrade level 
        self.P2level = upgrade[6]
        


    def action(self,plane,army,Earmy):#Increase the level of the upgrade for the respective player who pressed the button (found using plane)
        if plane == P1Plane: 
            self.P1level +=1
        elif plane == P2Plane:
            self.P2level +=1
        

    def update(self,army,events):#Display small bars on the screen to show what level the upgrade is at for each of the three upgrades
            i,j = 0,0
            while i < self.P1level:
                pygame.draw.rect(screen, grey,(120+i*40,575+(self.identifier * 50),30,5))
                i += 1
            while j < self.P2level:
                pygame.draw.rect(screen, grey,(870 + 230+j*40,575+(self.identifier * 50),30,5))
                j += 1

class Mlevel(Upgrade):
    def __init__(self):
        Upgrade.__init__(self,mlevel)

class Hlevel(Upgrade):
    def __init__(self):
        Upgrade.__init__(self,hlevel)

class Alevel(Upgrade):
    def __init__(self):
        Upgrade.__init__(self,alevel)

            

class SpawnUnit(Actions):
    def __init__(self,uniting):
        Actions.__init__(self,uniting)

    def action(self,plane,army,Earmy):
        if plane == P1Plane: #Spawn the unit for the respective player who pressed the button (found using plane)
            P1.army.add(Units(dic[self.key1]))
        else:
            P2.army.add(Units(dic[self.key2]))

    def update(self,army,events): #No update function for this class is used but will be called in action so a pass is required
        pass
    
class Inf(SpawnUnit):
    def __init__(self):
        SpawnUnit.__init__(self,inf)

class Tank(SpawnUnit):
    def __init__(self):
        SpawnUnit.__init__(self,tank)

class Rocket(SpawnUnit):
    def __init__(self):
        SpawnUnit.__init__(self,rocket)


