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
        
        # remove leaving guests
        self.guests = [g for g in self.guests if g != "leaving"]

        # move all the guests who want to move
        moving_guests_indices = [i for i in range(len(self.guests) - 1, -1, -1) if self.guests[i].moving_to != -1]
        for i in moving_guests_indices:
            to = self.guests[i].moving_to
            self.guests[i].moving_to = -1
            built_structures[to].guests.append(self.guests.pop(i))

        # update staff in random order
        indices = list(range(len(self.staff)))
        random.shuffle(indices)
        for i in indices:
            self.staff[i].step(built_structures, self, s_i, i)
        
        # move all staff who want to move
        moving_staff_indices = [i for i in range(len(self.staff) - 1, -1, -1) if self.staff[i].moving_to != -1]
        for i in moving_staff_indices:
            to = self.staff[i].moving_to
            self.staff[i].moving_to = -1
            built_structures[to].staff.append(self.staff.pop(i))
