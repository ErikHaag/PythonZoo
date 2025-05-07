from .animal_base import animal_base
import random

class tiger(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # el tigre
            self.happiness -= 4
        feeder_index = -1
        i = 0
        for staff in structureContext.staff:
            if staff.role == "feeder":
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
                    # tiger do nothin
                    if  self.happiness >= 40 or self.hunger >= 30:
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 20
                case "roar":
                    # tiger loud
                    if  self.happiness <= 39 and self.hunger >= 30:
                        self.hunger -= 2
                        self.happiness += 6
                        self.activity_timer = 1
                case "attack":
                    # tiger angry
                    if  self.happiness <= 39 and self.hunger <= 30:
                        self.hunger -= 2
                        self.happiness += 10
                        self.activity_timer = 10