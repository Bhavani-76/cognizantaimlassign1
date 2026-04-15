class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def __repr__(self):
        return f"Patient({self.name}, disease={self.disease})"
