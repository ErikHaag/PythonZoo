from .animal_base import animal_base
import random

class lion(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # the lion should not be let near small dogs
            self.happiness -= 4
        feeder_index = -1
        i = 0
        for staff in structureContext.staff:
            if staff.role == "feeder" and staff.activity_timer == 0 and staff.move_timer == 0:
                feeder_index = i
                break
            i += 1
        if self.hunger <= 30 and feeder_index != -1:
            self.happiness += 10
            structureContext.staff[feeder_index].activity_timer = 4
            self.activity_timer = 3
            return
        if random.random() >= 0.2:
            match random.choice(["laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "roar", "attack"]):
                case "laze":
                    # the lion understands the concept of hard work and chooses not to regardless
                    if  self.happiness >= 40 or self.hunger >= 30:
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 20
                case "roar":
                    # the lion has been banned from dave & busters for making speeches about his political views
                    if  self.happiness <= 39 and self.hunger >= 30:
                        self.hunger -= 2
                        self.happiness += 6
                        self.activity_timer = 1
                case "attack":
                    # the lion is angry
                    if  self.happiness <= 39 and self.hunger <= 30:
                        self.hunger -= 2
                        self.happiness += 10
                        self.activity_timer = 10