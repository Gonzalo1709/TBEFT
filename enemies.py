from inspect import Attribute, getattr_static, getmembers
import random
from types import MethodDescriptorType
from armors import *
from guns import *

def calc_pen_chance(penetration, armor):
    d = armor.durability / armor.maxDur * 100
    c = armor.aclass
    n = penetration
    a = (121-5000/(45+d*2))*c*10*0.01
    chance1 = (0.4*(a-n-15)**2)/100
    chance2 = (100+n/(0.9*a-n))/100
    if a-15 < n < a:
        return(chance1)
    elif a <= n:
        return(chance2)
    else:
        return(0)

class StandardHealth:
    
    def __init__(self):
        self.head = 35
        self.thorax = 85
        self.rArm = 60
        self.lArm = 60
        self.stomach = 70
        self.rLeg = 65
        self.lLeg = 65
        self.overall = self.head + self.thorax + self.rArm + self.lArm + self.stomach + self.rLeg + self.lLeg

        self.multipliers = {
            "rArm": 0.7,
            "lArm": 0.7,
            "lLeg": 1.0,
            "rLeg": 1.0,
            "stomach": 1.5,
            "head": 1,
            "thorax": 1
        }

        self.equiped_armor = False
        self.equiped_gun = False

    def equip_armor(self, type, durability):
        self.equiped_armor = active_armor(type, durability)

    def equip_gun(self, gun):
        self.equiped_gun = gun

    def getoverall(self):
        self.overall = self.head + self.thorax + self.rArm + self.lArm + self.stomach + self.rLeg + self.lLeg
        return(self.overall)

    def dealdamage(self, bodypart, gun_shot_from, armor=False,):
        damagetodeal = gun_shot_from.damage
        penetration = gun_shot_from.pen

        for i in self.__dict__.keys():

            invalid_attributes = ["overall", "multipliers", "equiped_gun", "equiped_armor"]
            if i.startswith("__") or i in invalid_attributes:
                pass
            else:
                if bodypart != i:
                    pass

                else:
                    if armor != False:
                        if bodypart in armor.protects:
                            pen_check = random.random()
                            pen_chance = calc_pen_chance(penetration, self.equiped_armor)
                            if pen_check >= 1-pen_chance:
                                damagetodeal *= 1-pen_chance
                                damagetodeal = int(round(damagetodeal, 0))
                            else:
                                damagetodeal = int(round(damagetodeal*0.2, 0))

                    if getattr(self, i)-damagetodeal > 0:
                        setattr(self, i, getattr(self, i)-damagetodeal)

                    else:
                        setattr(self, i, 0)
                        damagetodeal -= getattr(self, i)
                        damagetodeal *= self.multipliers[i]
                        alivelimbs = []
                        for i in self.__dict__.keys():
                            if i.startswith("__") or i in invalid_attributes:
                                pass
                            elif getattr(self, i) > 0:
                                alivelimbs.append(i)
                        damageperlimb = int(damagetodeal/len(alivelimbs))
                        for limb in alivelimbs:
                            if getattr(self, limb) - damageperlimb > 0:
                                setattr(self, limb, getattr(self, limb)-damageperlimb)
                            else:
                                setattr(self, limb, 0)


class PMC:
    def __init__(self, level, myself=False):
        self.level = level
        self.accmodpos = int(level/2)
        self.accmodneg =  int(level/2) - 12
        self.health = StandardHealth()
        if myself != False: #Things to happen to the player
            from myself import inv
            self.health.equip_gun(inv["gun"])
            self.health.equip_armor(inv["armor"], int(inv["armor"].durability/inv["armor"].maxDur*100))
        # First attempt to accuracy = round(random.randint(-(51-level),51-round(level/3, 0)) * 0.01 + 0.50, 2)


class Scav:
    scav_armors_type = ["paca", "zhuk", "thor"]
    scav_armors_durability = random.randint(50, 100)
    def __init__(self):
        self.accmodpos = random.randint(-50, 0)
        self.accmodneg = self.accmodpos - random.randint(0, 50)
        self.health = StandardHealth()
        self.health.equip_armor(self.scav_armors_type[random.randint(0,2)], self.scav_armors_durability)