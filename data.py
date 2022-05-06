import armors
import inspect

class PMCHealth:
    head = 35
    thorax = 85
    rArm = 60
    lArm = 60
    stomach = 70
    rLeg = 65
    lLeg = 65
    overall = head+thorax+rArm+lArm+stomach+rLeg+lLeg

class Armor:
    def __init__(self, type, currdurability):
        for x, obj in inspect.getmembers(armors):
            if inspect.isclass(obj):
                if obj.__name__ == type:
                    self.durability = obj.maxDur * currdurability * 0.01
                    self.name = obj.displayName
                    self.aclass = obj.aclass
