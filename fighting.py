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

    def firingsequence():
        aimpoint = 0
        tofire = int(inv["gun"].rof/100)
        print("         v           Fire with Ctrl+C", end="\n")
        print("-------------------", end="\r")
        speedofcursor = 0.3-(tofire/40)
        direction = True
        hits = 0
        close = 0
        while tofire > 0:
            try:
                while True:
                    if direction == True:
                        direction2 = False
                        while True:
                            if aimpoint == 19 or aimpoint == 0:
                                direction2 = not direction2
                            if direction2 == True:
                                aimpoint += 1
                            else:
                                aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(hits) + " Close: " + str(close) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)
                    else:
                        direction2 = True
                        while True:
                            if aimpoint == 19 or aimpoint == 0:
                                direction2 = not direction2
                            if direction2 == True:
                                aimpoint += 1
                            else:
                                aimpoint -= 1
                            lap = "-" * aimpoint
                            rap = "-" * (19-aimpoint)
                            fullaim = lap + "×" + rap + " On point: " + str(hits) + " Close: " + str(close) + " Left: " + str(tofire)
                            print(fullaim, end="\r")
                            time.sleep(speedofcursor)

            except KeyboardInterrupt:
                if aimpoint == 9:
                    hits += 1
                if aimpoint == 8 or aimpoint == 10:
                    close =+ 1
                tofire -= 1
                direction = not direction
                if direction == True:
                    aimpoint = 0
                else:
                    aimpoint = 19
                pass

        fullaim = lap + "×" + rap + " On point: " + str(hits) + " Close: " + str(close) + " Left: " + str(tofire)
        print(fullaim, end="\r")
        print("")
        print(f"You shot {hits} shots on point and {close} close!")
        return(hits, close)

    while myhealth.head > 0 and myhealth.thorax > 0 and enemy.health.head > 0 and enemy.health.thorax > 0:
        if turn == "me":
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
                firingsequence()
                #deal damage