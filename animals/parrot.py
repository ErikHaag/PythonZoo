from .animal_base import animal_base
import random

class parrot(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aviary":
            # Parrot need lots of room to fly.
            self.happiness -= 5
        has_feeder = False
        feeder_index = -1
        i = 0
        for staff in structureContext.staff:
            if staff.role == "feeder":
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
            match random.choice(["speak", "speak", "speak", "swear_like_a_sailor", "fly", "Fly", "dance", "collect object", "puzzle", "puzzle"]):
                case "speak":
                    # Bird like to talk
                    if (self.happiness <= 60 or self.hunger <= 70) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 0
                        self.happiness += 7
                        self.activity_timer = 1
                case "swear_like_a_sailor":
                    # Bird get mad sometimes
                    if self.happiness >= 10 and self.hunger >= 30:
                        self.hunger -= 5
                        self.happiness += 50
                        self.activity_timer = 20
                case "fly":
                    # Bird needs to fly
                    if (self.happiness <= 40 or self.hunger <= 70) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 35
                        self.happiness += 10
                        self.activity_timer = 15
                case "dance":
                    # he like to do a lil dance when happy
                    if (self.happiness <= 90 or self.hunger <= 100) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 1
                        self.happiness += 15
                        self.activity_timer = 1
                case "puzzle":
                    # Bird need activity
                    if (self.happiness >= 40) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 5
                        self.happiness += 10
                        self.activity_timer = 10
                case "collect_object":
                    # Bird need activity
                    if (self.happiness >= 40) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 5
                        self.happiness += 5
                        self.activity_timer = 5