"""create doctor crud opertaion"""
import sys
import os
from models.doctor import Doctor
from exceptions.doctor_not_found_exception import DoctorNotFoundException
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
        return self.doctors

    def get_doctor_by_id(self, doctor_id: int):
        """
        get a doctor by id
        """
        logger.info(f"Getting doctor with id: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found")
        return None

    def update_doctor(self, doctor_id: int, name: str = None, specialty: str = None):
        """
        update a doctor's information
        """
        logger.info(f"Updating doctor with id: {doctor_id}")
        doctor = self.get_doctor(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
                
    def delete_doctor(self, doctor_id: int):
        """
        delete a doctor from the store
        """
        logger.info(f"Deleting doctor with id: {doctor_id}")
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]