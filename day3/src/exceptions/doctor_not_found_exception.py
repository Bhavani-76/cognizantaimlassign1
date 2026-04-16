"""
create doctor not found exception to handle cases where a doctor is not found in the store
"""

class DoctorNotFoundException(Exception):
    """
    DoctorNotFoundException class to handle cases where a doctor is not found in the store
    """
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)