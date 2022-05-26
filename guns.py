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
    armor_damage = 0.33
    name = "HK MP5 9x19 submachine gun (Navy 3 Round Burst)"
    slots = 6

class adar:
    firemode = "semiauto"
    recoil = 149
    rof = 800
    effrecoil = round(recoil * rof / RECOIL_MODIFIER_BASELINE, 2)
    #damage and pen for m855
    damage = 50
    pen = 28
    magsize = 30
    armor_damage = 0.37
    name = "ADAR 2-15 5.56x45 carbine"
    slots = 8