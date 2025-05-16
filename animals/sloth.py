from .animal_base import animal_base
import random

class sloth(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # bro is generally unaware
            self.happiness -= 4
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
            match random.choice(["laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "laze", "crawl_kinda"]):
                case "laze":
                    # sloths dont do much
                    if  self.happiness >= 25 or self.hunger >= 15:
                        self.hunger -= 1
                        self.happiness += 1
                        self.activity_timer = 30
                case "crawl_kinda":
                    # they move a little bit
                    if  self.happiness < 25 and self.hunger < 15:
                        self.hunger -= 1
                        self.happiness += 2
                        self.activity_timer = 30