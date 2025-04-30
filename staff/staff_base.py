from master import built_structures

class staff_base:
    def __init__(self):
        self.move_timer = 0
        self.role = ""
    
    def step(self, structureContext):
        if self.move_timer >= 0:
            self.move(structureContext)
        else:
            self.move_timer -= 1