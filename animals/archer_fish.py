from .animal_base import animal
import random

class archer_fish(animal):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aquarium":
            # the fish doesn't like to be in a bag somewhere.
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
            match random.choice(["spit_human", "spit_human", "spit_human", "leap", "leap"]):
                case "spit_human":
                    # the fish is very moody
                    if (self.happiness <= 10 or self.hunger <= 30) and (len(structureContext.guests) >= 1 or len(structureContext.staff) >= 1):
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 1
                case "leap":
                    # today I learned they will sometimes jump!
                    if self.happiness <= 70 and self.hunger >= 80:
                        self.hunger -= 2
                        self.happiness += 6
                        self.activity_timer = 2