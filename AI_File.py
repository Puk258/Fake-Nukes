from pygame import *
from Functions import *
from Constants import *
import Unit, random


def AI():
 #AI Possible spawning sequences
 TMM = [P2Tank,P2Rocket,P2Rocket]
 III = [P2Inf,P2Inf,P2Inf]
 IMIM = [P2Inf,P2Rocket,P2Inf,P2Rocket]
 #Variables used by AI spawner
 ESpawnList = [TMM,III,IMIM] #list of above sequences
 ESpnNxt = random.randrange(0,len(ESpawnList)) #Randdomly picks which sequence to run:
 ESpawnCounter = 0
 


 if P2.money >= ESpawnList[ESpnNxt][ESpawnCounter][5] and P2.AIToggle and P2.spawnpos:
            P2.army.add(Unit.Units(ESpawnList[ESpnNxt][ESpawnCounter])) #Spawn the next unit denoted by the spawn next sequence from the spawn list
            P2.money -= ESpawnList[ESpnNxt][ESpawnCounter][5]
            ESpawnCounter += 1
            if ESpawnCounter == len(ESpawnList[ESpnNxt]): # If the counter is the same size as the Spawn list, then randomly decide which spawn list to run next.
                ESpnNxt = random.randrange(0,len(ESpawnList))
                ESpawnCounter = 0


