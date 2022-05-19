RECOIL_MODIFIER_BASELINE = 227500 #Based on effective recoil of the SA-58

class mp5:
    firemode = "fullauto"
    recoil = 73
    rof = 800
    effrecoil = round(recoil * rof / RECOIL_MODIFIER_BASELINE, 2)
    #damage and pen for pst gzh
    damage = 54
    pen = 20
    magsize = 30
    slots = 8
    armor_damage = 0.33