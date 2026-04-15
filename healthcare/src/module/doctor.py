class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return f"Doctor({self.name}, specialization={self.specialization})"
