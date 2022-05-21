class esmarch:
    uses = 1
    max_uses = 1
    does = ["removes heavy bleeds"]
    name = "Esmarch tourniquet"
    description = "The hemostatic tourniquet is named after Friedrich August von Esmarch, who proposed its use, along with other methods in military field surgery."
    type = "one time"
    def use(self):
        self.uses -= 1
        if self.uses <= 0:
            del self
    slots = 1

class calok_b:
    uses = 3
    max_uses = 3
    does = ["removes heavy bleeds"]
    name = "CALOK-B hemostatic applicator"
    description = "CALOK-B Applicator hemostatic agent allows you to inject hemostatic granules through a wound opening directly to the source of bleeding in just a few seconds."
    type = "one time"
    def use(self):
        self.uses -= 1
        if self.uses <= 0:
            del self
    slots = 1

class bandage:
    uses = 1
    max_uses = 1
    does = ["removes light bleeds"]
    name = "Aseptic bandage"
    description = "The most common gauze bandage, autoclaved and aseptic."
    type = "one time"
    def use(self):
        self.uses -= 1
        if self.uses <= 0:
            del self
    slots = 1

class army_bandage:
    uses = 2
    max_uses = 2
    does = ["removes light bleeds"]
    name = "Army bandage"
    description = "Army-issue gauze bandage."
    type = "one time"
    def use(self):
        self.uses -= 1
        if self.uses <= 0:
            del self
    slots = 1

class car_medkit:
    uses = 220
    max_uses = 220
    does = ["heals", "removes light bleeds"]
    name = "Car first aid kit"
    description = "Like a fire extinguisher, car first aid kit is crucially important protection measure in the event of an emergency on the road."
    type = "heal kit"
    max_heal_amount = 70
    def use(self, heal_amount):
        self.uses -= heal_amount
        if self.uses <= 0:
            del self
    slots = 2

class ai2:
    uses = 100
    max_uses = 100
    does = ["heals"]
    name = "AI-2 medkit"
    description = "The AI-2 medikit was developed as a standard service first aid kit for various defence and law enforcement agencies and civil defense forces of USSR. In case of all-out conflict with the use of weapons of mass destruction it should have been distributed to the population of the affected and surrounding areas."
    type = "heal kit"
    max_heal_amount = 50
    def use(self, heal_amount):
        self.uses -= heal_amount
        if self.uses <= 0:
            del self
    slots = 1

class cms:
    uses = 5
    max_uses = 5
    does = ["surgery"]
    name = "CMS surgical kit"
    description = "Compact surgical kit for treatment of bullet wounds and other serious injuries."
    type = "surgery kit"
    min_hp_loss = 0.55
    max_hp_loss = 0.75
    def use(self):
        self.uses -= 1 
        if self.uses <= 0:
            del self
    slots = 2

class surv12:
    uses = 15
    max_uses = 15
    does = ["surgery", "removes fractures"]
    name = "Surv12 field surgical kit"
    description = "Advanced surgical kit with additional and better tools, allowing you to treat serious injuries right on the battlefield."
    type = "surgery kit"
    min_hp_loss = 0.28
    max_hp_loss = 0.40
    def use(self):
        self.uses -= 1 
        if self.uses <= 0:
            del self
    slots = 3