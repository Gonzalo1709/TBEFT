from enemies import *
from myself import inv, myhealth
from threading import Event
import time

exit = Event()

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
        while not exit.is_set():
            while aimpoint < 20:
                lap = "-" * aimpoint
                rap = "-" * aimpoint
                print(lap, "×", rap, end="\r")
                aimpoint += 1
                time.sleep(0.2)
            while aimpoint > 0:
                lap = "-" * aimpoint
                rap = "-" * aimpoint
                print(lap, "×", rap, end="\r")
                aimpoint -= 1
                time.sleep(0.2)