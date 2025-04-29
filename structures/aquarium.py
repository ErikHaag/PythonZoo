from .structure_base import structure

class aquarium(structure):
    def __init__(self, name : str):
        super().__init__(name)
        self.type = "aquarium"