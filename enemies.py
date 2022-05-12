import random

class PMC:
    def __init__(self, level):
        self.level = level
        self.accmodpos = int(level/2)
        self.accmodneg =  int(level/2) - 12
        # First attempt to accuracy = round(random.randint(-(51-level),51-round(level/3, 0)) * 0.01 + 0.50, 2)

class StandardHealth:
    head = 35
    thorax = 85
    rArm = 60
    lArm = 60
    stomach = 70
    rLeg = 65
    lLeg = 65
    overall = head+thorax+rArm+lArm+stomach+rLeg+lLeg

class Scav:
    def __init__(self):
        self.accmodpos = random.randint(-50, 0)
        self.accmodneg = self.accmodpos - random.randint(0, 50)