from .animal_base import animal_base
import random

class elephant(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # elephant not supposed to be under water
            self.happiness -= 4
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
            match random.choice(["sit", "sit", "sit", "charge", "pfooooot"]):
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
                case "pfooooot":
                    # :D
                    if  self.happiness >= 60 and self.hunger >= 60:
                        self.hunger -= 1
                        self.happiness += 15
                        self.activity_timer = 5