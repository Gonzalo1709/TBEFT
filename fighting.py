from enemies import PMC, Scav, StandardHealth
from myself import inv, myself
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
        hits = []
        close = []
        noshot = []
        missed = []
        while tofire > 0:
            try:
                while tofire > 0:

                    if direction == True:
                        while aimpoint < 19:
                            aimpoint += 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(len(hits)) + " Close: " + str(len(close)) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                        noshot.append(tofire)
                        tofire -= 1
                        direction = not direction
                        aimpoint = 19

                    else:
                        while aimpoint > 0:
                            aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(len(hits)) + " Close: " + str(len(close)) + " Left: " + str((tofire))
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                        noshot.append(tofire)
                        tofire -= 1
                        direction = not direction
                        aimpoint = 0

            except KeyboardInterrupt:
                if aimpoint == 9:
                    hits.append(tofire)
                elif aimpoint == 8 or aimpoint == 10:
                    close.append(tofire)
                else:
                    missed.append(tofire)
                tofire -= 1
                direction = not direction
                if direction == True:
                    aimpoint = 0
                else:
                    aimpoint = 19
                pass


        fullaim = lap + "×" + rap + " On point: " + str(len(hits)) + " Close: " + str(len(close)) + " Left: " + str(tofire)
        print(fullaim, end="\r")
        print("")
        print(f"You shot {len(hits)} shots on point and {len(close)} close! {len(missed)} were missed and {len(noshot)} weren't fired.")
        
        sequence = []
        for i in range(int(inv["gun"].rof/100)):
            sequence.append("-")
        for i in hits:
            sequence[i-1] = "h"
        for i in close:
            sequence[i-1] = "c"
        for i in noshot:
            sequence[i-1] = "-"
        for i in missed:
            sequence[i-1] = "m"

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
                enemy.health.end_of_round()
                myself.health.end_of_round()
                turn = "them"

            if choice == 2:
                print("--------------------")
                print("Action to do:      -")
                print("-1. Reposition     -")
                print("-2. Hold angle     -")
                print("--------------------")
                action = int(input("Input choice (1-2): "))