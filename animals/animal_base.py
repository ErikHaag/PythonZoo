class animal:
    def __init__(self):
        # look at that animal!
        self.happiness = 100
        self.hunger = 100
        self.activity_timer = 0
    
    def step(self):
        # update animal's stats every minute
        self.happiness -= 1
        self.hunger -= 1
        self.activity_timer -= 1
        if self.activity_timer <= 0:
            # only start activity when not already doing one
            self.maybe_do_activity()
    
    def maybe_do_activity(self):
        # do action, with certain actions being more important. 
        pass