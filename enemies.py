from inspect import Attribute, getattr_static, getmembers
import random
from types import MethodDescriptorType

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
            "stomach": 1.5
        }

    def getoverall(self):
        self.overall = self.head + self.thorax + self.rArm + self.lArm + self.stomach + self.rLeg + self.lLeg
        return(self.overall)

    def dealdamage(self, bodypart, damage):
        damagetodeal = damage

        for i in self.__dict__.keys():
            if i.startswith("__") or i == "overall" or i == "multipliers":
                pass
            else:
                if bodypart != i:
                    pass
                else:
                    if getattr(self, i)-damage > 0:
                        setattr(self, i, getattr(self, i)-damagetodeal)
                    else:
                        setattr(self, i, 0)
                        damagetodeal -= getattr(self, i)
                        damagetodeal *= self.multipliers[i]
                        alivelimbs = []
                        for i in self.__dict__.keys():
                            if i.startswith("__") or i == "overall" or i == "multipliers":
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
    def __init__(self, level):
        self.level = level
        self.accmodpos = int(level/2)
        self.accmodneg =  int(level/2) - 12
        self.health = StandardHealth()
        # First attempt to accuracy = round(random.randint(-(51-level),51-round(level/3, 0)) * 0.01 + 0.50, 2)


class Scav:
    def __init__(self):
        self.accmodpos = random.randint(-50, 0)
        self.accmodneg = self.accmodpos - random.randint(0, 50)
        self.health = StandardHealth()