from .animal_base import animal_base
import random

class giraffe(animal_base):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # Land and need lots of room
            self.happiness -= 8
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
            structureContext.staff[feeder_index].activity_timer = 4
            self.activity_timer = 3
            return
        if random.random() >= 0.2:
            match random.choice(["walk", "walk", "walk", "walk", "waLK", "rest", "rest", "fight"]):
                case "walk":
                    # idk man these guys just be walking all the time they lowkey lame
                    if  self.happiness >= 40 or self.hunger >= 50:
                        self.hunger -= 1
                        self.happiness += 5
                        self.activity_timer = 5
                case "rest":
                    # nap time
                    if  self.happiness >= 70 and self.hunger >= 80:
                        self.hunger -= 1
                        self.happiness += 15
                        self.activity_timer = 10
                case "fight":
                    # when they get really upset they start neck slapping eachother
                    if  self.happiness <= 20 and self.hunger <= 30:
                        self.hunger -= 5
                        self.happiness += 4
                        self.activity_timer = 2