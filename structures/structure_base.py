class structure_base:
    def __init__(self, name : str):
        self.animals = []
        self.guests = []
        self.staff = []
        self.name = name
        self.type = ""
    
    def step(self, s_i):
        for animal in self.animals:
            animal.step(self)

        i = 0
        for guest in self.guests:
            guest.step(self, s_i, i)
            i += 1
        
        i = 0
        for staff in self.staff:
            staff.step(self, s_i, i)
            i += 1