class animal:
    def __init__(self):
        # look at that animal!
        self.happiness = 100
        self.hunger = 100
    
    def step(self):
        # update animal's stats every minute
        self.happiness -= 1
        self.hunger -= 1