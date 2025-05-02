from .animal_base import animal_base
import random

class kiwi(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aviary":
            # i dont think these things can fly but they're birds and frankly thats all that matters
            self.happiness -= 5
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
            match random.choice(["wander", "wander",  "wander", "wander", "wander", "wander", "lay_egg"]):
                case "wander":
                    # this thing literally doesnt do anything at all
                    if (self.happiness >= 30 or self.hunger >= 10):
                        self.hunger -= 1
                        self.happiness += 1
                        self.activity_timer = 1
                case "lay_egg":
                    # well i mean its gotta at some point that thing is huge
                    if self.happiness >= 1 and self.hunger < 10:
                        self.hunger -= 5
                        self.happiness += 50
                        self.activity_timer = 20