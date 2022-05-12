from enemies import *
from myself import inv, myhealth
import time


def fight(enemy, kindofencounter):

    from main import clear


    print(f"Battle with {type(enemy).__name__} has begun!")

    if kindofencounter == "mefirst":
        print("You saw them first so it's your turn!")
        turn = "me"
    if kindofencounter == "themfirst":
        print("They saw you first. It's their turn!")
        turn = "them"



    while myhealth.head > 0 and myhealth.thorax > 0 and enemy.health.head > 0 and enemy.health.thorax > 0:
        aimpoint = 0
        tofire = int(inv["gun"].rof/100)
        lap = "-" * aimpoint
        rap = "-"*(20-aimpoint)
        print("         v            Fire with Ctrl+C", end="\n")
        print("--------------------", end="\r")
        speedofcursor = 0.3-(tofire/40)
        direction = True
        hits = 0
        while tofire > 0:
            try:
                while True:
                    if direction == True:
                        direction2 = False
                        while True:
                            if aimpoint == 20 or aimpoint == 0:
                                direction2 = not direction2
                            if direction2 == True:
                                aimpoint += 1
                            else:
                                aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (20-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(hits) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                    else:
                        direction2 = True
                        while True:
                            if aimpoint == 20 or aimpoint == 0:
                                direction2 = not direction2
                            if direction2 == True:
                                aimpoint += 1
                            else:
                                aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (20-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(hits) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)

            except KeyboardInterrupt:
                if aimpoint == 10 or aimpoint == 9 or aimpoint == 11:
                    hits += 1
                tofire -= 1
                direction = not direction
                if direction == True:
                    aimpoint = 0
                else:
                    aimpoint = 20
                pass
        fullaim = lap + "×" + rap + " On point: " + str(hits) + " Left: " + str(tofire) + "" + str(aimpoint)
        print(fullaim, end="\r")
        print("")
        print(f"You shot {hits} shots on point!")