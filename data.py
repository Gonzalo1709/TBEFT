import armors
import inspect

class Armor:
    def __init__(self, type, currdurability):
        #type of armor between quotation marks. isnt considered object yet program just matches name
        for x, obj in inspect.getmembers(armors):
            if inspect.isclass(obj):
                if obj.__name__ == type:

                    self.durability = obj.maxDur * currdurability * 0.01
                    self.name = obj.displayName
                    self.aclass = obj.aclass