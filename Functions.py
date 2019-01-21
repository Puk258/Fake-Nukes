from pygame import *
from Constants import *

# Checks to see if there is a unit in the spawn zone, if there is retrun false

# Sounds
rifle = pygame.mixer.Sound("Sounds&Music/m4shoot.wav")
missile = pygame.mixer.Sound("Sounds&Music/missile.wav")
tank = pygame.mixer.Sound("Sounds&Music/Tank.wav")
fighter = pygame.mixer.Sound("Sounds&Music/Fighter.wav")

def CheckSpawn(army):
     for unit in army:
        if unit.rect.x <50 or unit.rect.x > 1200:
            return False
        else:
            continue
     return True

#Checks to see if anything dead in the army. Will add money to arg 2
def ClearDead(army,Emoney,Emlevel):
     for a in army:
          if a.health <=0:
                  Emoney += (150*(1+(0.1*Emlevel)))
                  a.kill()
     return Emoney

def MoveAttack(army,Earmy,alevel,Ehlevel):
    for unit1 in army:
        if unit1.index == "Shell" or unit1.index == "EShell": # For the shells, if it goes below a certain point, kill the sprite and damage any enemies with range of the shell
            if unit1.rect.midleft[1] > 275:
                for Eunit in Earmy:
                    if Eunit.rect[0]<unit1.rect[0]+240 and Eunit.rect[0]>unit1.rect[0]-240:
                        Eunit.health -=(25*(1+(0.1*alevel))*(1-(0.1*Ehlevel)))

                unit1.health = 0
        unit1.speed = speeds[unit1.index] # Set the speed initially to the units default speed, found in the dictionary speeds
        unit1.current_frames = unit1.move_sprite_list
        for unit2 in army:
            if unit1.index == "P2Inf" or unit1.index =="P2Tank" or unit1.index =="P2Rocket":
                direction = -1
            else:
                direction = 1
            if unit2 != unit1 and unit2.rect.colliderect(unit1.rect) and direction*unit2.rect.midleft[0] > direction*unit1.rect.midleft[0]:
                unit1.speed = [0,0] #For allied troops, if there is someone infront of the unit, set speed to 0. The direction is determined by the team.
                unit1.frame = 0
        for Eunit in Earmy:
            if unit1.index == "P1Rocket": #For enemy Troops, if enemy is directly infront of you, set speed to 0 and attack. If a Rocket, always attack once they are close enough  but keep walking
                if Eunit.rect.midleft[0]-unit1.rect.midleft[0] < 250:
                    if Eunit.index == "P2Tank": #Rockets do more damage to tanks but less damage to normal men. Damage is also affected by the upgrade levels of the players
                        Eunit.health -= 0.7*(1+(0.1*alevel))*(1-(0.1*Ehlevel))
                    else:
                        Eunit.health -= 0.4*(1+(0.1*alevel))*(1-(0.1*Ehlevel))
            elif unit1.index == "P2Rocket":
                if Eunit.rect.midleft[0]-unit1.rect.midleft[0] > -250:
                    if Eunit.index == "P1Tank":
                        Eunit.health -= 0.7*(1+(0.1*alevel))*(1-(0.1*Ehlevel))
                    else:
                        Eunit.health -= 0.4*(1+(0.1*alevel))*(1-(0.1*Ehlevel))
            if unit1.rect.colliderect(Eunit.rect): #If unit1 collides with an enemy then stop, switch to the firing animation and damage the enemy
                if unit1.index == "P1Tank" or unit1.index =="P2Tank":
                     tank.play()
                unit1.speed = [0,0]
                unit1.current_frames = unit1.fire_sprite_list
                Eunit.health -= 1*(1+(0.1*alevel))*(1-(0.1*Ehlevel))
