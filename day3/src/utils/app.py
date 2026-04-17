import sys 
import os
#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)

from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from src.store.doctorstore import DoctorStore
from src.store.patientstore import PatientStore
from src.store.appointmentstore import AppointmentStore
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.exceptions.patient_not_found_exception import PatientNotFoundException
from src.exceptions.appointment_not_found_exception import AppointmentNotFoundException


from conf.logger_conf import setup_logger
"""
Entry point for the appliaction. This module initializes the application and starts the main loop.
"""
logger = setup_logger()

def doctor_app():
    """
    doctor app
    """
    logger.info("Doctor app run")
    doctor_store = DoctorStore()
    doctor1 = Doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = Doctor(2, "Dr. Johnson", "Neurology")
    doctor3 = Doctor(3, "Dr. Williams", "Pediatrics")

    doctor_store.add_doctor(doctor1)
    doctor_store.add_doctor(doctor2)
    doctor_store.add_doctor(doctor3)
    logger.info(f"added 3 doctors")

    #read - get all doctors
    logger.info("--read - get all doctors--")
    all_doctors = doctor_store.get_all_doctors()
    for doctor in all_doctors:
        logger.info(f"Retrieved doctor: {doctor}")
    #read - get doctor by id
    logger.info("--read - get doctor by id--")
    retrieved_doctor = doctor_store.get_doctor_by_id(1)
    logger.info(f"Retrieved doctor by id: {retrieved_doctor}")
    #update doctor
    logger.info("--update doctor--")
    updated_doctor = doctor_store.update_doctor(1, name="Dr. Smith Updated", specialty="Cardiology Updated")
    logger.info(f"Updated doctor: {updated_doctor}")
    #delete doctor
    logger.info("--delete doctor--")
    deleted_doctor = doctor_store.delete_doctor(1)
    logger.info(f"Deleted doctor: {deleted_doctor}")
    logger.info(f"remaining doctors: {len(doctor_store.get_all_doctors())}")
    #error handling - get doctor by id
    logger.info("--error handling - get doctor by id--")
    try:
        doctor_store.update_doctor(999, "Non-existent")
    except DoctorNotFoundException as e:
        logger.error(f"exception caught: {e}")
    return doctor_store
def patient_app():
    """
    patient app
    """
    from datetime import date
    #create -add patients
    logger.info("Patient app run")
    patient_store = PatientStore()
    patient1 = Patient(1, "John Doe", date(1990, 1, 1), "Hypertension")
    patient2 = Patient(2, "Jane Doe", date(1995, 5, 5), "Diabetes")
    patient3 = Patient(3, "Jim Doe", date(2000, 10, 10), "Asthma")

    patient_store.add_patient(patient1)
    patient_store.add_patient(patient2)
    patient_store.add_patient(patient3)
    logger.info(f"added 3 patients")

    #read - get all patients
    logger.info("--read - get all patients--")
    all_patients = patient_store.get_all_patients()
    for patient in all_patients:
        logger.info(f"Retrieved patient: {patient}")

    #read- get patient by id
    logger.info("--read- get patient by id--")
    all_patients = patient_store.get_all_patients()
    for patient in all_patients:
        logger.info(f"Retrieved patient: {patient}")
    
    #delete patient
    logger.info("--delete patient--")
    deleted_patient = patient_store.delete_patient(1)
    logger.info(f"Deleted patient: {deleted_patient}")
    logger.info(f"remaining patients: {len(patient_store.get_all_patients())}")
   
   
    #error handling - get patient by id
    logger.info("--error handling - get patient by id--")
    try:
        patient_store.get_patient(999)
    except PatientNotFoundException as e:
        logger.error(f"exception caught: {e}")
    return patient_store
def appointment_app(doctor_store, patient_store):
    """
    appointment app
    """
    logger.info("Appointment app run")
    appointment_store = AppointmentStore()
    from datetime import datetime, date

    #get doctor and patient for appointments
    doctors = list(doctor_store.get_all_doctors())
    patients = patient_store.get_all_patients()
    
    #create - add appointments
    logger.info("--create - add appointments--")
    # Note: doctor 1 and patient 1 were deleted in their respective functions, 
    # so we only have 2 doctors and 2 patients available
    if len(doctors) >= 2 and len(patients) >= 2:
        appointment1 = Appointment(1, patients[0], doctors[0], date(2024, 6, 1), datetime(2024, 6, 1, 10, 0).time())
        appointment2 = Appointment(2, patients[1], doctors[1], date(2024, 6, 2), datetime(2024, 6, 2, 11, 0).time())
        
        appointment_store.add_appointment(appointment1)
        appointment_store.add_appointment(appointment2)
        logger.info(f"added 2 appointments")
    else:
        logger.warning(f"Not enough doctors or patients to create appointments")
        logger.warning(f"Available doctors: {len(doctors)}, Available patients: {len(patients)}")
        return appointment_store

    #read - get all appointments
    logger.info("--read - get all appointments--")
    all_appointments = appointment_store.get_all_appointments()
    for appointment in all_appointments:
        logger.info(f"Retrieved appointment: {appointment}")
    #update appointment
    logger.info("--update appointment--")
    updated_appointment = appointment_store.update_appointment(1, appointment1)
    logger.info(f"Updated appointment: {updated_appointment}")
    #delete appointment
    logger.info("--delete appointment--")
    deleted_appointment = appointment_store.delete_appointment(1)
    logger.info(f"Deleted appointment: {deleted_appointment}")
    logger.info(f"remaining appointments: {len(appointment_store.get_all_appointments())}")
    #error handling - get appointment by id
    logger.info("--error handling - get appointment by id--")
    try:       
         appointment_store.get_appointment_by_id(999)
    except AppointmentNotFoundException as e:
        logger.error(f"exception caught: {e}")
    return appointment_store

def run():
    """
    test logger
    """
    logger.info("starting healthcare application")
    doctor_store = doctor_app()
    patient_store = patient_app()
    appointment_store = appointment_app(doctor_store, patient_store)
    logger.info("healthcare application run completed successfully")
    
""" handle entry point """
if __name__ == "__main__":
    run()

