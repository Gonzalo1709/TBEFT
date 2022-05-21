from guns import *
from armors import *
from items import *

level = 1

inv = {
    "gun": mp5,
    "armor": active_armor("trooper", 100),
    "items": [calok_b(), car_medkit(), army_bandage(), cms(), calok_b()]
}

from enemies import PMC

myself = PMC(level, True)
myself.health.is_player = True


#Works like this but dont forget to add parenthesis to inventory items.
print("--")
print(inv["items"])
print(inv["items"][0].uses)
print(inv["items"][4].uses)
inv["items"][0].use()
inv["items"][0].use()
inv["items"][0].use()
print(inv["items"])
print(inv["items"][0].uses)
print(inv["items"][4].uses)