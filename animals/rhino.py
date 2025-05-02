from .animal_base import animal_base
import random

class rhino(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # rhino not supposed to be under water
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
            match random.choice(["sit", "sit", "sit", "charge", "charge"]):
                case "sit":
                    # he does nothing for he is bored
                    if  self.happiness >= 30 or self.hunger >= 20:
                        self.hunger -= 1
                        self.happiness += 1
                        self.activity_timer = 5
                case "charge":
                    # anger
                    if  self.happiness < 30 and self.hunger < 20:
                        self.hunger -= 5
                        self.happiness += 10
                        self.activity_timer = 20