from enemies import PMC, Scav, StandardHealth
from myself import clean_inventory, inv, myself
import time
import random
from armors import *
from guns import *



def fight(enemy, kindofencounter):

    from main import clear

    print(f"Battle with {type(enemy).__name__} has begun!")

    if kindofencounter == "mefirst":
        print("You saw them first so it's your turn!")
        turn = "me"
    if kindofencounter == "themfirst":
        print("They saw you first. It's their turn!")
        turn = "them"

    def firingsequence(aimzone):
        if aimzone == 1:
            bodypart = random.randint(2, 4)
        else:
            bodypart = random.randint(5, 6)
        aimpoint = 0
        damage_to_deal = []
        deviation = int(inv["gun"].effrecoil)
        tofire = int(inv["gun"].rof/100)
        print("         v           Fire with Ctrl+C", end="\n")
        print("-------------------", end="\r")
        speedofcursor = 0.3-(tofire/40)
        direction = True
        sequence = []
        while tofire > 0:
            try:
                while tofire > 0:

                    if direction == True:
                        while aimpoint < 19:
                            aimpoint += 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(sequence.count("h")) + " Close: " + str(sequence.count("c")) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                        sequence.append("-")
                        tofire -= 1
                        direction = not direction
                        aimpoint = 19

                    else:
                        while aimpoint > 0:
                            aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(sequence.count("h")) + " Close: " + str(sequence.count("c")) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                        sequence.append("-")
                        tofire -= 1
                        direction = not direction
                        aimpoint = 0

            except KeyboardInterrupt:
                if aimpoint == 9:
                    sequence.append("h")
                elif aimpoint == 8 or aimpoint == 10:
                    sequence.append("c")
                else:
                    sequence.append("m")
                tofire -= 1
                direction = not direction
                if direction == True:
                    aimpoint = 0
                else:
                    aimpoint = 19
                pass


        fullaim = lap + "×" + rap + " On point: " + str(sequence.count("h")) + " Close: " + str(sequence.count("c")) + " Left: " + str(tofire)
        print(fullaim, end="\r")
        print("")
        print(f"You shot {sequence.count('h')} shots on point and {sequence.count('c')} close! {sequence.count('m')} were missed and {sequence.count('-')} weren't fired.")

        originalbodypart = bodypart
        shot = 1
        for i in sequence:

            accuracymod = random.randint(myself.accmodneg, myself.accmodpos)
            checkforhit = random.randint(-100, 100) + accuracymod

            typeofshot = "on point"

            if i == "c":
                checkforhit -= 33
                bodypart += round(random.uniform(-1, 1)+deviation, 0)
                typeofshot = "close"
            elif i == "-":
                if bodypart > originalbodypart:
                    bodypart -= 1
                elif bodypart < originalbodypart:
                    bodypart += 1
                print(f"Shot {shot} was unfired.")
                shot += 1
                continue
            elif i == "m":
                round(random.uniform(-1, 1)+deviation, 0)
                print(f"Shot {shot} missed.")
                shot += 1
                continue

            if bodypart >= 8:
                bodypart -= round(random.uniform(0, 2)+deviation, 0)
            elif bodypart <= -1:
                bodypart += round(random.uniform(0, 2)+deviation, 0)

            print(f"Shot {shot} was {typeofshot} and it ", end="")


            if checkforhit > 0:
                if bodypart == 1:
                    damage_to_deal.append("head")
                    print("hit the head!")
                    bodypart += round(random.uniform(-1, 1)+deviation, 0)
                elif bodypart >= 2 and bodypart <= 4:
                    if random.randint(0, 2) == 0:
                        damage_to_deal.append("thorax")
                        print("hit the thorax.")
                    elif round(random.random(), 0) == 0:
                        damage_to_deal.append("rArm")
                        print("hit the right arm.")
                    else:
                        damage_to_deal.append("lArm")
                        print("hit the left arm.")
                    bodypart += round(random.uniform(-1, 1)+deviation, 0)
                elif bodypart == 5:
                    damage_to_deal.append("stomach")
                    print("hit the stomach.")
                    bodypart += round(random.uniform(-1, 1)+deviation, 0)
                elif bodypart >= 6 and bodypart <= 7:
                    if round(random.random(), 0) == 1:
                        print("hit the right leg.")
                        damage_to_deal.append("rLeg")
                    else:
                        damage_to_deal.append("lLeg")
                        print("hit the left leg.")
                    bodypart += round(random.uniform(-1, 1)+deviation, 0)
                else:
                    bodypart += round(random.uniform(-1, 1)+deviation, 0)
                    if bodypart > 7:
                        print("missed! Your PMC shot too low!")
                    else:
                        print("missed! Your PMC shot too high!")
            else:
                print("missed!")
            shot += 1
        return(damage_to_deal)

    while myself.health.head > 0 and myself.health.thorax > 0 and enemy.health.head > 0 and enemy.health.thorax > 0:
        if turn == "me":
            print("")
            print("Your enemy seems to be wearing:")
            print(f"{enemy.health.equiped_armor.name} ({enemy.health.equiped_armor.durability}/{enemy.health.equiped_armor.maxDur})")
            print("--------------------")
            print("--Your turn begins--")
            print("--Choose an option--")
            print("--------------------")
            print("-1. Fire (end turn)-")
            print("-2. Action         -")
            print("-3. Inventory      -")
            print("-4. Attempt to flee-")
            print("--------------------")

            choice = int(input("Input choice (1-4): "))

            if choice == 1:
                print("--------------------")
                print("Body part to aim at:")
                print("-1. Upper body     -")
                print("-2. Lower body     -")
                print("--------------------")
                aimzone = int(input("Input choice (1-2): "))
                damage_to_deal = firingsequence(aimzone)
                for i in damage_to_deal:          
                    enemy.health.dealdamage(i, inv["gun"], enemy.health.equiped_armor)
                    check_for_bleed = random.random()
                    if check_for_bleed <= 0.25:
                        if check_for_bleed <= 0.125:
                            enemy.health.status_effects.append("heavy_bleed")
                        else:
                            enemy.health.status_effects.append("light_bleed")
                enemy.health.end_of_round()
                myself.health.end_of_round()
                turn = "them"

            elif choice == 2:
                print("--------------------")
                print("Action to do:      -")
                print("-1. Reposition     -")
                print("-2. Hold angle     -")
                print("--------------------")
                print("WARNING: THIS OPTION CURRENTLY DOES NOTHING")
                action = int(input("Input choice (1-2): "))

            elif choice == 3:
                clean_inventory()
                print("--------------------")
                print("Your inventory:")
                for index, item in enumerate(inv["items"]):
                    print(f'{index + 1}. {item.name} ({item.uses}/{item.max_uses})')
                print("--------------------")
                print("Select item to use or")
                print("0 to go back.")
                amount_of_items = len(inv["items"])
                item_to_use = int(input(f"Item to choose (0-{amount_of_items}): "))
                if item_to_use == 0:
                    pass
                elif item_to_use - 1 > amount_of_items:
                    print("Not a valid item.")
                else:
                    actions = False
                    if "heals" in inv["items"][item_to_use-1].does:
                        healable_limbs = []
                        alive_limbs = myself.health.get_alive_limbs()
                        for limb in alive_limbs:
                            if getattr(myself.health, limb) < myself.health.max_hp[limb]:
                                healable_limbs.append(limb)
                        if len(healable_limbs) == 0:
                            if len(inv['items'][item_to_use-1].does) == 1:
                                print("No limbs to heal.")
                            else:
                                pass
                        else:
                            print("Which limb would you like to heal?: ")
                            for index, limb in enumerate(healable_limbs):
                                limb_translations = {"head": "Head", "thorax": "Thorax", "rArm": "Right arm", "lArm": "Left arm", "stomach": "Stomach", "lLeg": "Left leg", "rLeg": "Right leg"}
                                print(f"{index+1}. {limb_translations[limb]} ({getattr(myself.health, limb)}/{myself.health.max_hp[limb]})")
                            print("0. Go back.")
                            limb_to_heal = int(input(f"Limb to heal (0-{len(healable_limbs)}): "))
                            if limb_to_heal == 0:
                                pass
                            elif limb_to_heal - 1> len(healable_limbs):
                                print("Not a valid limb.")
                            else:
                                myself.health.use_heal(healable_limbs[limb_to_heal-1], inv["items"][item_to_use-1])
                                actions = True

                    if "removes heavy bleeds" in inv["items"][item_to_use-1].does:
                        if "heavy_bleed" in myself.health.status_effects:
                            myself.health.use_esmarch()
                            inv["items"][item_to_use-1].use()
                            actions = True
                        else:
                            if len(inv['items'][item_to_use-1].does) == 1:
                                print("You don't have heavy bleeds to heal.")
                    
                    if "removes light bleeds" in inv["items"][item_to_use-1].does:
                        if "light_bleed" in myself.health.status_effects:
                            myself.health.use_bandage()
                            inv["items"][item_to_use-1].use()
                            actions = True
                        else:
                            if len(inv['items'][item_to_use-1].does) == 1:
                                print("You don't have light bleeds to heal.")

                    if "surgery" in inv["items"][item_to_use-1].does:
                        healable_limbs = myself.health.get_surgery_compatible_limbs()
                        if len(healable_limbs) == 0:
                            if len(inv['items'][item_to_use-1].does) == 1:
                                print("No limbs to do surgery on.")
                            else:
                                pass
                        else:
                            print("Which limb would you like to do surgery on?: ")
                            for index, limb in enumerate(healable_limbs):
                                limb_translations = {"head": "Head", "thorax": "Thorax", "rArm": "Right arm", "lArm": "Left arm", "stomach": "Stomach", "lLeg": "Left leg", "rLeg": "Right leg"}
                                print(f"{index+1}. {limb_translations[limb]} ({getattr(myself.health, limb)}/{myself.health.max_hp[limb]})")
                            print("0. Go back.")
                            limb_to_heal = int(input(f"Limb to heal (0-{len(healable_limbs)}): "))
                            if limb_to_heal == 0:
                                pass
                            elif limb_to_heal - 1> len(healable_limbs):
                                print("Not a valid limb.")
                            else:
                                myself.health.use_surgery(inv["items"][item_to_use-1], healable_limbs[limb_to_heal-1])
                                actions = True

                    if actions == False:
                        print("The item you selected had no available actions.")
            
            elif choice == 4:
                print("Option not yet implemented.")

            else:
                print("Not a valid option.")

        elif turn == "them":
            def enemyfire():
                
            enemy.health.getoverall()
            if enemy.health.overall >= 330:
                
