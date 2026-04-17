"""
patient not found exception
"""
class PatientNotFoundException(Exception):
    def __init__(self, patient_id):
        self.patient_id = patient_id
        super().__init__(f"Patient with ID {patient_id} not found")
