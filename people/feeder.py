from master import *
from .staff_base import staff_base

class feeder(staff_base):
    def __init__(self):
        super().__init__()
        self.role = "feeder"
    
    def maybe_move(self, structureContext, structure_i, staff_i):
        global built_structures
        
        smallest_local_hunger = 100
        for animal in structureContext.animals:
            if animal.hunger < smallest_local_hunger:
                smallest_local_hunger = animal.hunger
        
        smallest_hunger = 100
        new_structure_index = 0
        for structure in built_structures:
            for animal in structure:
                if animal.hunger < smallest_hunger:
                    smallest_hunger_index = new_structure_index
            new_structure_index += 1
        if smallest_hunger < smallest_local_hunger - 10:
            built_structures[smallest_hunger_index].staff.append(built_structures[structure_i].pop(staff_i))