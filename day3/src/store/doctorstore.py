"""create doctor crud opertaion"""
import sys 
import os
#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)

from src.models.doctor import Doctor
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from conf.logger_conf import setup_logger
"""
Entry point for the appliaction. This module initializes the application and starts the main loop.

"""
logger = setup_logger()
class DoctorStore:
    """
    DoctorStore class to manage doctor records
    """
    def __init__(self):
        self.doctors = {}
        
    def add_doctor(self, doctor: Doctor):
        """
        add a doctor to the store
        """
        logger.info(f"Adding doctor: {doctor}")
        self.doctors[doctor.id] = doctor

    def get_all_doctors(self):
        """
        get all doctors
        """
        logger.info("Getting all doctors")
        return self.doctors.values()

    def get_doctor_by_id(self, doctor_id: int):
        """
        get a doctor by id
        """
        logger.info(f"Getting doctor with id: {doctor_id}")
        for doctor in self.doctors.values():
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(doctor_id)

    def update_doctor(self, doctor_id: int, name: str = None, specialty: str = None):
        """
        update a doctor's information
        """
        logger.info(f"Updating doctor with id: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
                
    
    def delete_doctor(self, doctor_id):
        if doctor_id not in self.doctors:
            raise DoctorNotFoundException(doctor_id)
        del self.doctors[doctor_id]

        