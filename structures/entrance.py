from .structure_base import structure

class entrance(structure):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "entrance"