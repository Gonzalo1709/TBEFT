from guns import *
from armors import *

level = 1

inv = {
    "gun": mp5,
    "armor": active_armor("trooper", 100)
}

from enemies import PMC

myself = PMC(level, True)
myself.health.is_player = True