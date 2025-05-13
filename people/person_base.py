# from master import built_structures

class person_base:
    def __init__(self):
        self.move_timer = 0
        self.activity_timer = 0
    
    def step(self, structureContext, s_i, p_i):
        if self.activity_timer >= 0 and self.move_timer >= 0:
            self.maybe_move(structureContext, s_i, p_i)
        if self.move_timer < 0:
            self.move_timer -= 1
        if self.activity_timer < 0:
            self.move_timer -= 1
    
    def maybe_move(self, structureContext, s_i, p_i):
        pass