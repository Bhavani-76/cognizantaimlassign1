"""
create doctor not found exception to handle cases where a doctor is not found in the store
"""

class DoctorNotFoundException(Exception):
    def __init__(self, doctor_id):
        self.doctor_id = doctor_id
        super().__init__(f"Doctor with ID {doctor_id} not found")
