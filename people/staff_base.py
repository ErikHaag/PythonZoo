from .person_base import person

class staff(person):
    def __init__(self):
        super().__init__()
        self.role = ""