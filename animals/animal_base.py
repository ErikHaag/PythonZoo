class animal:
    def __init__(self, name : str):
        # look at that animal!
        self.activity_timer = 0
        self.happiness = 100
        self.hunger = 100
        self.name = name
    
    def step(self, structureContext):
        # update animal's stats every minute
        self.happiness -= 1
        self.hunger -= 1
        self.activity_timer -= 1
        if self.activity_timer <= 0:
            # only start activity when not already doing one
            self.maybe_do_activity(structureContext)
        if self.hunger < 0:
            self.hunger = 0
            self.happiness -= 10
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.happiness > 100:
            self.happiness
    
    def maybe_do_activity(self, structureContext):
        # do action, with certain actions being more important. 
        pass