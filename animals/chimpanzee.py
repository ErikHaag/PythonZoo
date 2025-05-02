from .animal_base import animal_base
import random

class chimpanzee(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # monkey not supposed to be under water
            self.happiness -= 4
        has_feeder = False
        for staff in structureContext.staff:
            if staff.role == "feeder":
                has_feeder = True
                break
        if self.hunger <= 30 and has_feeder:
            self.hunger += 50
            self.happiness += 10
            self.activity_timer = 3
            return
        if random.random() >= 0.2:
            match random.choice(["fling", "scream", "scream", "climb", "climb"]):
                case "scream":
                    # the monkey is pissed probably
                    if  self.happiness <= 40 or self.hunger <= 50:
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 1
                case "climb":
                    # movin and groovin
                    if  self.happiness <= 70 and self.hunger >= 80:
                        self.hunger -= 2
                        self.happiness += 6
                        self.activity_timer = 20
                case "fling":
                    # when they get really upset they start flinging around some less than savory things on the ground
                    if  self.happiness <= 20 and self.hunger <= 30:
                        self.hunger -= 2
                        self.happiness += 10
                        self.activity_timer = 5