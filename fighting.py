from enemies import *
from inventory import inv

def fight(enemy):
    print(f"Battle with {enemy} has begun!")
    tofire = int(inv["gun"].rof/100)