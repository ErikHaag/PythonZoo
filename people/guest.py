from .person_base import person_base

import random

class guest(person_base):
    def __init__(self):
        super().__init__()
        self.structures_seen = ["entrance"]
    
    def maybe_move(self, built_structures, structureContext, s_i, p_i):
        if len(self.structures_seen) > 10 or len(self.structures_seen) >= len(built_structures) :
            # leave zoo
            built_structures[s_i].guests[p_i] = "gone"
            return
        structure_indices = list(range(len(built_structures)))
        random.shuffle(structure_indices)
        for i in structure_indices:
            s = built_structures[i]
            if s.name not in self.structures_seen:
                self.structures_seen.append(s.name)
                built_structures[i].guests.append(built_structures[s_i].guests[p_i])
                built_structures[s_i].guests[p_i] = "gone"
                return