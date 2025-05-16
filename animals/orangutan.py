from .animal_base import animal_base
import random

class orangutan(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # monkey not supposed to be under water
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
            match random.choice(["contemplate", "contemplate", "contemplate", "contemplate", "drive_golf_cart", "climb", "climb"]):
                case "contemplate":
                    # the orangutan is a modern day philosopher
                    if  self.happiness >= 75 or self.hunger >= 60:
                        self.hunger -= 1
                        self.happiness += 10
                        self.activity_timer = 15
                case "climb":
                    # movin and groovin
                    if  self.happiness < 75 and self.hunger >= 60:
                        self.hunger -= 5
                        self.happiness += 5
                        self.activity_timer = 20
                case "drive_golf_cart":
                    # only other creatures on earth that I have ever seen driving a car
                    if  self.happiness >= 75 and self.hunger < 60:
                        self.hunger -= 2
                        self.happiness += 15
                        self.activity_timer = 30