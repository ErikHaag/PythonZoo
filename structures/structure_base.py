import random

class structure_base:
    def __init__(self, name : str):
        self.animals = []
        self.guests = []
        self.staff = []
        self.name = name
        self.type = ""
    
    def step(self, built_structures, s_i):
        # update animals in random order
        indices = list(range(len(self.animals)))
        random.shuffle(indices)
        for i in indices:
            self.animals[i].step(self)
        
        # update guests in random order
        indices = list(range(len(self.guests)))
        random.shuffle(indices)
        for i in indices:
            self.guests[i].step(built_structures, self, s_i, i)
        # remove moved guest
        self.guests = [g for g in self.guests if self.guests != "gone"]

        # update staff in random order
        indices = list(range(len(self.staff)))
        random.shuffle(indices)
        for i in indices:
            self.staff[i].step(built_structures, self, s_i, i)
        # remove moved guests
        self.guests = [s for s in self.staff if self.staff != "gone"]