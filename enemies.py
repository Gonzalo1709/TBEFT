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

        self.max_hp = {
            "rArm": 60,
            "lArm": 60,
            "lLeg": 65,
            "rLeg": 65,
            "stomach": 70,
            "head": 35,
            "thorax": 85,
            "overall": 440
        }

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
        self.status_effects = []
        self.is_player = False

    def equip_armor(self, type, durability):
        self.equiped_armor = active_armor(type, durability)

    def equip_gun(self, gun):
        self.equiped_gun = gun

    def getoverall(self):
        self.overall = self.head + self.thorax + self.rArm + self.lArm + self.stomach + self.rLeg + self.lLeg
        return(self.overall)

    def dealdamage(self, bodypart, gun_shot_from, armor=False,):
        damagetodeal = gun_shot_from.damage
        original_damage = gun_shot_from.damage
        penetration = gun_shot_from.pen

        for i in self.__dict__.keys():

            invalid_attributes = ["overall", "multipliers", "equiped_gun", "equiped_armor", "status_effects", "is_player", "max_hp"]
            if i.startswith("__") or i in invalid_attributes:
                pass
            else:
                if bodypart != i:
                    pass

                else:
                    pen_event = False
                    armor_damage = False
                    if armor != False and self.equiped_armor.name != "Nothing":
                        if bodypart in armor.protects:
                            armor_damage = True
                            pen_check = random.random()
                            pen_chance = calc_pen_chance(penetration, self.equiped_armor)
                            if pen_check >= 1-pen_chance:
                                if pen_chance * 0.90 > 0.70:
                                    damagetodeal *= pen_chance*0.90
                                    damagetodeal = int(round(damagetodeal, 0))
                                else:
                                    damagetodeal *= 0.70
                                    damagetodeal = int(round(damagetodeal, 0))
                                pen_event = True
                            else:
                                damagetodeal = int(round(damagetodeal*0.1, 0))

                    if getattr(self, i)-damagetodeal > 0:
                        setattr(self, i, getattr(self, i)-damagetodeal)

                    else:
                        setattr(self, i, 0)
                        damagetodeal -= getattr(self, i)
                        damagetodeal *= self.multipliers[i]
                        alivelimbs = self.get_alive_limbs()
                        damageperlimb = int(damagetodeal/len(alivelimbs))
                        for limb in alivelimbs:
                            if getattr(self, limb) - damageperlimb > 0:
                                setattr(self, limb, getattr(self, limb)-damageperlimb)
                            else:
                                setattr(self, limb, 0)
                    
                    if armor_damage == True:
                        if pen_event == True:
                            self.equiped_armor.durability -=  original_damage * self.equiped_armor.destructibility *  0.88 * pen_chance * gun_shot_from.armor_damage
                        else:
                            self.equiped_armor.durability -=  original_damage * self.equiped_armor.destructibility * pen_chance * gun_shot_from.armor_damage
                        if self.equiped_armor.durability < 0:
                            self.equiped_armor.durability = 0

    def get_alive_limbs(self):
        invalid_attributes = ["overall", "multipliers", "equiped_gun", "equiped_armor", "status_effects", "is_player", "max_hp"]
        alive_limbs = []
        for i in self.__dict__.keys():
            if i.startswith("__") or i in invalid_attributes:
                pass
            elif getattr(self, i) > 0:
                alive_limbs.append(i)
        return(alive_limbs)

    def get_surgery_compatible_limbs(self):
        valid_attributes = ["rArm", "lArm", "stomach", "rLeg", "lLeg"]
        surgery_compatible = []
        for i in self.__dict__.keys():
            if i not in valid_attributes:
                pass
            elif getattr(self, i) <= 0:
                surgery_compatible.append(i)
        return(surgery_compatible)
    
    def heavy_bleed(self):
        alive_limbs = self.get_alive_limbs()
        damage_per_limb = random.randint(3, 4)
        for limb in alive_limbs:
            if getattr(self, limb) - damage_per_limb > 0:
                setattr(self, limb, getattr(self, limb)-damage_per_limb)
            else:
                setattr(self, limb, 0)

    def light_bleed(self):
        alive_limbs = self.get_alive_limbs()
        damage_per_limb = random.randint(1, 3)
        for limb in alive_limbs:
            if getattr(self, limb) - damage_per_limb > 0:
                setattr(self, limb, getattr(self, limb)-damage_per_limb)
            else:
                setattr(self, limb, 0)

    def end_of_round(self):
        for i in self.status_effects:
            if i == "heavy_bleed":
                self.heavy_bleed()
                if self.is_player == True:
                    print("You have an untreated heavy bleed!")
                else:
                    print("Your enemy left behind a blood trail.")
            elif i == "light_bleed":
                self.light_bleed()
                if self.is_player == True:
                    print("You have an untreated light bleed!")
                else:
                    print("Your enemy left behind a blood trail.")
    
    def use_esmarch(self, item):
        completed = False
        for index, item in enumerate(self.status_effects):
            if completed == False and item == "heavy_bleed":
                self.status_effects.pop(index)
                completed = True
                item.use()
                print("You patched up one of your heavy bleeds.")

    def use_bandage(self, item):
        completed = False
        for index, element in enumerate(self.status_effects):
            if completed == False and element == "light_bleed":
                self.status_effects.pop(index)
                completed = True
                item.use()
                print("You patched up one of your light bleeds.")

    def use_surgery(self, item, limb_to_operate):
        if limb_to_operate in ["stomach", "rLeg", "lLeg", "rLeg", "lLeg"] and getattr(self, limb_to_operate) <= 0:
            setattr(self, limb_to_operate, 1)
            self.max_hp[limb_to_operate] *= random.randint(item.min_hp_loss, item.max_hp_loss)
            item.use()
            print(f"You performed surgery on your {limb_to_operate} and restored it to 1hp.")

    def use_heal(self, bodypart_to_heal, item):
        if getattr(self, bodypart_to_heal) > 0 and getattr(self, bodypart_to_heal) < self.max_hp[bodypart_to_heal]:
            if getattr(self, bodypart_to_heal) + item.max_heal_amount <= self.max_hp[bodypart_to_heal]:
                if item.uses <= item.max_heal_amount:
                    setattr(self, bodypart_to_heal, getattr(self, bodypart_to_heal) + item.uses)
                    print(f"You healed your {bodypart_to_heal} for {item.uses}.")
                    item.use(item.uses)
                else:
                    setattr(self, bodypart_to_heal, getattr(self, bodypart_to_heal) + item.max_heal_amount)
                    print(f"You healed your {bodypart_to_heal} for {item.max_heal_amount}.")
                    item.use(item.max_heal_amount)
            else:
                used = self.max_hp[bodypart_to_heal] - getattr(self, bodypart_to_heal)
                setattr(self, bodypart_to_heal, self.max_hp[bodypart_to_heal])
                item.use(used)
                print(f"You healed your {bodypart_to_heal} for {used}.")
        else:
            print("That limb is not able to be healed.")

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
    scav_armors_type = ["paca", "zhuk", "thor", "nothing"]
    scav_armors_durability = round(random.randint(50, 100), 0)
    def __init__(self):
        self.accmodpos = random.randint(-50, 0)
        self.accmodneg = self.accmodpos - random.randint(0, 50)
        self.health = StandardHealth()
        self.health.equip_armor(self.scav_armors_type[random.randint(0, len(self.scav_armors_type)-1)], self.scav_armors_durability)