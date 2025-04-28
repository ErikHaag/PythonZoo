from animal_base import animal

class archer_fish(animal):
    def maybe_do_activity(self, structureContext):
        if structureContext.type != "aquarium":
            self.happiness -= 4
        has_feeder = False
        for staff in structureContext.staff:
            if staff.role == "feeder":
                has_feeder = True
                break
        if self.hunger <= 30 and has_feeder:
            self.hunger += 50
            self.activity_timer = 3
        