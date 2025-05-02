from .person_base import person_base

class staff_base(person_base):
    def __init__(self):
        super().__init__()
        self.role = ""