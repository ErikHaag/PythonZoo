class structure:
    def __init__(self, name : str):
        self.animals = []
        self.guests = []
        self.staff = []
        self.name = name
        self.type = ""
    
    def step(self):
        for animal in self.animals:
            animal.step(self)
        
        for guest in self.guests:
            guest.step(self)
        
        for staff in self.staff:
            staff.step(self)