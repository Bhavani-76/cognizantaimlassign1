"""
create patient crud opertaion
"""
import sys 
import os
#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)


from conf.logger_conf import setup_logger
"""
Entry point for the appliaction. This module initializes the application and starts the main loop.

"""
logger = setup_logger()
from src.exceptions.patient_not_found_exception import PatientNotFoundException

class PatientStore:

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def get_patient(self, patient_id):
        if patient_id not in self.patients:
            raise PatientNotFoundException(patient_id)
        return self.patients[patient_id]

    def update_patient(self, patient_id, updated_patient):
        if patient_id not in self.patients:
            raise PatientNotFoundException(patient_id)
        self.patients[patient_id] = updated_patient

    def delete_patient(self, patient_id):
        if patient_id not in self.patients:
            raise PatientNotFoundException(patient_id)
        del self.patients[patient_id]