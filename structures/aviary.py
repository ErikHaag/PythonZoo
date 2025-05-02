from .structure_base import structure_base

class aviary(structure_base):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "avairy"