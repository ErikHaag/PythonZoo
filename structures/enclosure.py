from .structure_base import structure

class enclosure(structure):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "enclosure"