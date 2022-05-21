from guns import *
from armors import *
from items import *

level = 1

inv = {
    "gun": mp5,
    "armor": active_armor("trooper", 100),
    "items": [calok_b(), car_medkit(), army_bandage(), cms(), calok_b()]
}

def clean_inventory():   
    for index, item in enumerate(inv["items"]):
        if item.uses == 0:
            del inv['items'][index]

from enemies import PMC

myself = PMC(level, True)
myself.health.is_player = True