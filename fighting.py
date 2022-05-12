from enemies import *
from myself import inv, myhealth

def fight(enemy, kindofencounter):


    print(f"Battle with {type(enemy).__name__} has begun!")

    if kindofencounter == "mefirst":
        print("You saw them first so it's your turn!")
        turn = "me"
    if kindofencounter == "themfirst":
        print("They saw you first. It's their turn!")
        turn = "them"

    tofire = int(inv["gun"].rof/100)

    while myhealth.head > 0 and myhealth.thorax > 0 and enemy.health.head > 0 and enemy.health.thorax > 0:

        pass
        #remove pass when working, its in there to stop getting an error for empty while loop.
