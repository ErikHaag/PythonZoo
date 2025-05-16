from .animal_base import animal_base
import random

class pigeon(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aviary":
            # bird need lots of room to fly.
            self.happiness -= 5
        has_feeder = False
        feeder_index = -1
        i = 0
        for staff in structureContext.staff:
            if staff.role == "feeder" and staff.activity_timer == 0 and staff.move_timer == 0:
                feeder_index = i
                break
            i += 1
        if self.hunger <= 30 and feeder_index != -1:
            self.hunger += 50
            self.happiness += 10
            structureContext.staff[feeder_index].activity_timer = 2
            self.activity_timer = 3
            return
        if random.random() >= 0.2:
            match random.choice(["search", "search", "search", "sing", "sing", "sing", "sing", "pester", "fly", "fly", "fly", "fly", "fly", "fly", "fly", "fly", ]):
                case "sing":
                    # Bird like to sing
                    if  self.happiness <= 60 or self.hunger <= 70:
                        self.happiness += 7
                        self.activity_timer = 1
                case "fly":
                    # Bird needs to fly
                    if self.happiness <= 40 or self.hunger <= 70: 
                        self.hunger -= 35
                        self.happiness += 10
                        self.activity_timer = 15
                case "search":
                    # bird sorta looks around and sees whats up
                    if self.hunger < 40:
                        self.hunger -= 1
                        self.happiness += 15
                        self.activity_timer = 1
                case "pester":
                    # bird hate you
                    if (self.happiness < 20) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 3