class structure:
    def __init__(self):
        self.animals = {}
        self.guests = {}
        self.staff = {}
    
    def step(self):
        for animal in self.animals:
            animal.step()
        
        for guest in self.guests:
            guest.step()
        
        for staff in self.staff:
            staff.step()