from .staff_base import staff_base

import random

class feeder(staff_base):
    def __init__(self):
        super().__init__()
        self.role = "feeder"
    
    def maybe_move(self, built_structures, structureContext, structure_i, staff_i):
        # find the lowest hunger of an animal in the same structure
        smallest_local_hunger = 100
        for animal in structureContext.animals:
            if animal.hunger < smallest_local_hunger:
                smallest_local_hunger = animal.hunger
        
        # find the lowest hunger of any animal in the zoo, and where it is
        smallest_hunger = 100
        smallest_hunger_index = 0
        i = 0
        for structure in built_structures:
            for animal in structure.animals:
                if animal.hunger < smallest_hunger:
                    smallest_hunger = animal.hunger
                    smallest_hunger_index = i
            i += 1
        # if global hunger is smaller than the local one, then move
        if smallest_hunger + 10 < smallest_local_hunger:
            self.move_timer = random.randint(2)
            self.moving_to = smallest_hunger_index
            return