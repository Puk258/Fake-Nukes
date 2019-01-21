import random
from Buttons import *

AIToggle = False
Quit = False
Font = pygame.font.SysFont("calibri", 25)
statfont = pygame.font.SysFont("calibri", 15)
immortalmoney = 300
killmoney = 100
upmmoney, uphmoney,upamoney = 150,150,150
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

class Team(): # Sets up the players with all the necessary varaibles and counters used in the game
    def __init__(self):
        self.army = sprite.Group()
        self.money = 3600
        self.immortalcount = 5
        self.spawnpos = True

class P1(Team):
    def __init__(self):
        super().__init__()
        self.Diff = 0
        self.start = True


class P2(Team):
    def __init__(self):
        super().__init__()
        self.AIToggle = False



Players = []
P1 = P1()
P2 = P2()
Players.append(P1)
Players.append(P2)

#Defines some colours
SCREENWIDTH = 1366
SCREENHEIGHT = 705
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
LIGHTGREY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (100, 0, 0)

#This is where all the different attributes of the different units are all set up in the format shown below
# stats=[health,filename,posit,speed,attack,cost,index]
P1Inf = [100,"Sprites/P1/Infantry/Move/P1InfMove.png", (-100, 340),[3,0], 0 ,100, "P1Inf", "Sprites/P1/Infantry/Fire/P1InfFire.png"]
P1Tank = [200,"Sprites/P1/Tank/Move/P1TankMove.png",(-100, 250),[3,0],0,150,"P1Tank", "Sprites/P1/Tank/Fire/P1TankFire.png"]
P1Rocket = [15,"Sprites/P1/Rocket/Move/P1RocketMove.png",(-100,340),[3,0],0,75,"P1Rocket", "Sprites/P1/Rocket/Fire/P1RocketFire.png"]
P1Plane = [1000,"Sprites/P1/Fighter/FighterP1.png",[0,15],[12,0],0,500,"P1Plane","Sprites/P1/Fighter/FighterP1.png"]
P2Inf = [100,"Sprites/P2/Infantry/Move/P2InfMove.png", (1260,340),[-3,0], 0 ,100, "P2Inf", "Sprites/P2/Infantry/Fire/P2InfFire.png"]
P2Tank = [200,"Sprites/P2/Tank/Move/P2TankMove.png",(1260,340),[-3,0],0,150,"P2Tank", "Sprites/P2/Tank/Fire/P2TankFire.png"]
P2Rocket = [15,"Sprites/P2/Rocket/Move/P2RocketMove.png",(1260,340),[-3,0],0,75,"P2Rocket", "Sprites/P2/Rocket/Fire/P2RocketFire.png"]
P2Plane = [1000,"Sprites/P2/Fighter/FighterP2.gif",[1260,50],[-12,0],0,500,"P2Plane","Sprites/P2/Fighter/FighterP2.gif"]
Shell = [ 1000, "Sprites/Shell.png", [0, 0], [0, 30], 0, 0, 'Shell', "Sprites/Shell.png"]

#Variables defining where the buttons will be placed on the Y axis
spawnbuttonypos = 559
powerbuttonypos = 645
upgradexpos = 10
upgradeh = 48


void1 = MenuButton("Wealth",983,555,100,upgradeh,brown,red,upmmoney)
void2 = MenuButton("Health",983,605,100,upgradeh,brown,red,uphmoney)
void3 = MenuButton("Attack",983,655,100,upgradeh,brown,red,upamoney)

#This is where the buttons for the main part of the game are defined in the format as shown below.
#Button key values [xpos, ypos, width, height, colour]
Infbutton = SpawnButton("Inf",508,spawnbuttonypos,110,80,brown,red,image.load("Sprites/STANDPlayer1.gif"),150, 10, 5,100,"Rocket","Tank")
Tankbutton = SpawnButton("Tank",628,spawnbuttonypos,110,80,brown,red,image.load("Sprites/P1/Tank/Move/P1TankMove1.gif"), 500, 5, 10,150,"Infantry","Rocket")
Rocketbutton = SpawnButton("Rocket",748,spawnbuttonypos,110,80,brown,red,image.load("Sprites/P1/Rocket/Fire/P1RokFire1.gif"), 100, 10, 20,75,"Tank","Infantry")
strikebutton = MenuButton("Airstrike",508,powerbuttonypos,110,55,brown,red,P1Plane[5])
killbutton = MenuButton("Assasinate",628,powerbuttonypos,110,55,brown,red, killmoney)
immortalbutton = MenuButton(("Medics"),748,powerbuttonypos,110,55,brown,red,immortalmoney)
Upmoneybutton = MenuButton("Wealth",upgradexpos,555,100,upgradeh,brown,red , upmmoney)
Uphealthbutton = MenuButton("Health",upgradexpos,605,100,upgradeh,brown,red, uphmoney)
Upattackbutton = MenuButton("Attack",upgradexpos,655,100,upgradeh,brown,red, upamoney)



#This dictionary is used to define the default speeds of all of the units
speeds = {"P1Inf":P1Inf[3], "P1Tank":P1Tank[3], "P1Rocket":P1Rocket[3],"P1Plane":P1Plane[3],"Shell":Shell[3],  "P2Inf":P2Inf[3],"P2Tank":P2Tank[3],"P2Rocket":P2Rocket[3],"P2Plane":P2Plane[3]}
