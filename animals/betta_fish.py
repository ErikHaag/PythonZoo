from .animal_base import animal_base
import random

class betta_fish(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aquarium":
            # the fish doesn't like to be in a bag somewhere.
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
            match random.choice(["plot_evilly", "fight", "fight", "fight", "fight", "fight", "fight", "fight", "fight", "fight", ]):
                case "plot_evilly":
                    # the fish is very evil
                    if  self.happiness >= 70 or self.hunger >= 80:
                        self.happiness -= 10
                        self.activity_timer = 5
                case "fight":
                    # kill each other
                    if self.happiness < 70 and self.hunger < 80:
                        self.hunger -= 10
                        self.happiness += 5
                        self.activity_timer = 10