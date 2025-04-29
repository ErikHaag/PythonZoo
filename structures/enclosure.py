from .structure_base import structure

class enclosure(structure):
    def __init__(self):
        super().__init__()
        self.type = "enclosure"