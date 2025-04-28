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
    
    def maybe_do_activity(self, structureContext):
        # do action, with certain actions being more important. 
        pass