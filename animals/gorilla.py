from .animal_base import animal_base
import random

class gorilla(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # monkey not supposed to be under water
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
            match random.choice(["contemplate", "contemplate", "contemplate", "contemplate", "beat_chest", "hoot", "holler"]):
                case "contemplate":
                    # unlike the orangutan the gorilla subcribes to western philosophy
                    if  self.happiness >= 75 or self.hunger >= 60:
                        self.hunger -= 1
                        self.happiness += 10
                        self.activity_timer = 15
                case "beat_chest":
                    # beatin that shit up
                    if  self.happiness < 75 and self.hunger >= 60:
                        self.hunger -= 5
                        self.happiness += 5
                        self.activity_timer = 20
                case "hoot":
                    # sometimes gorilla need to hoot
                    if  self.happiness >= 75 and self.hunger < 60:
                        self.hunger -= 2
                        self.happiness += 15
                        self.activity_timer = 30
                case "holler":
                    # sometimes gorilla need to holler at yo girl
                    if  self.happiness <= 50 and self.hunger < 40:
                        self.hunger -= 2
                        self.happiness += 10
                        self.activity_timer = 20