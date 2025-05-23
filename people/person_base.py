# from master import built_structures

class person_base:
    def __init__(self):
        self.activity_timer = 0
        self.move_timer = 0
        self.moving_to = -1
    
    def step(self, built_structures, structureContext, s_i, p_i):
        if self.activity_timer >= 0 and self.move_timer >= 0:
            self.maybe_move(built_structures, structureContext, s_i, p_i)
        if self.moving_to == -1 and self.move_timer < 0:
            self.move_timer -= 1
        if self.activity_timer < 0:
            self.move_timer -= 1
    
    def maybe_move(self, built_structures, structureContext, s_i, p_i):
        pass