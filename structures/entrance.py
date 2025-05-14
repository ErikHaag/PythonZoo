from .structure_base import structure_base
from people.guest import guest

import random

class entrance(structure_base):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "entrance"
    
    def step(self, s_i):
        super().step(s_i)
        for _ in range(random.randint(0, 3)):
            self.guests.append(guest())