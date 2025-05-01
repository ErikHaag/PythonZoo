from .animal_base import animal
import random

class giraffe(animal):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "enclosure":
            # Land and need lots of room
            self.happiness -= 8
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