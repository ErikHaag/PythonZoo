from .animal_base import animal
import random

class sloth(animal):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # bro is generally unaware
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