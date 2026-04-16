"""
define a Doctor class with attributes id, name, and specialty. Include a __str__ method to provide a string representation of the Doctor object.
"""
class Doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty
    def __str__(self):
        return f"Doctor(id={self.id}, name={self.name}, specialty={self.specialty})"