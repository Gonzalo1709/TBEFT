import inspect
import armors

class active_armor:
    def __init__(self, type, currdurability):
        #type of armor between quotation marks. isnt considered object yet program just matches name
        for x, obj in inspect.getmembers(armors):
            if inspect.isclass(obj):
                if obj.__name__ == type:
                    self.durability = obj.maxDur * currdurability * 0.01
                    self.maxDur = obj.maxDur
                    self.name = obj.displayName
                    self.aclass = obj.aclass
                    self.slots = obj.slots
                    self.protects = obj.protects

class paca:
    aclass = 2
    maxDur = 50
    displayName = "PACA Soft Armor"
    slots = 9
    protects = ["thorax", "stomach"]

class zhuk:
    aclass = 3
    maxDur = 50
    displayName = 'BNTI "Zhuk-3" body armor (Press)'
    slots = 9
    protects = ["thorax", "stomach"]

class trooper:
    aclass = 4
    maxDur = 85
    displayName = 'HighCom Trooper TFO body armor (Multicam)'
    slots = 9
    protects = ["thorax", "stomach"]

class thor:
    aclass = 4
    maxDur = 35
    displayName = 'NFM THOR Concealable Reinforced Vest body armor'
    slots = 9
    protects = ["thorax", "stomach"]

class korund:
    aclass = 5
    maxDur = 45
    displayName = 'NPP KlASS "Korund-VM" body armor'
    slots = 12
    protects = ["thorax", "stomach"]

class gzhel:
    aclass = 5
    maxDur = 65
    displayName = 'BNTI "Gzhel-K" body armor'
    slots = 9
    protects = ["thorax", "stomach"]

class zhuk6:
    aclass = 6
    maxDur = 75
    displayName = 'BNTI "Zhuk-6a" body armor'
    slots = 9
    protects = ["thorax", "stomach"]