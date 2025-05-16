from .animal_base import animal_base
import random

class deer(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # deer doesnt go in the aquarium
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
            match random.choice(["sit", "sit", "graze", "graze", "graze", "strange_deer_noise"]):
                case "sit":
                    # he does nothing for he is bored
                    if  self.happiness >= 30 or self.hunger >= 20:
                        self.hunger -= 1
                        self.happiness += 1
                        self.activity_timer = 5
                case "graze":
                    # they be wanderin
                    if  self.happiness < 30 and self.hunger < 20:
                        self.hunger -= 5
                        self.happiness += 10
                        self.activity_timer = 20
                case "strange_deer_noise":
                    # ive heard the noise before but its for sure not a noise that makes sense
                    if  self.happiness >= 60 and self.hunger >= 60:
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 5