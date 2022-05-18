from guns import *
from enemies import StandardHealth, PMC
from armors import *

level = 1

inv = {
    "gun": mp5,
    "armor": active_armor("trooper", 100),
}

myself = PMC(level)