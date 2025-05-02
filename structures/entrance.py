from .structure_base import structure_base

class entrance(structure_base):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "entrance"