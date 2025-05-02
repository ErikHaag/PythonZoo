from .animal_base import animal_base
import random

class capybara(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # they pretty chill
            self.happiness -= 1
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
            match random.choice(["chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "chill", "meander"]):
                case "chill":
                    # they like to chill
                    if  self.happiness >= 0 or self.hunger > 0:
                        self.hunger -= 0
                        self.happiness += 5
                        self.activity_timer = 10
                case "meander":
                    # sometimes they move
                    if  self.happiness < 25 and self.hunger < 15:
                        self.hunger -= 1
                        self.happiness += 6
                        self.activity_timer = 12