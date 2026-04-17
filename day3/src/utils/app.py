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


from conf.logger_conf import setup_logger
"""
Entry point for the appliaction. This module initializes the application and starts the main loop.

"""
logger = setup_logger()


def run():
    """
    test logger
    """
    from datetime import datetime, date
    doctor1 = Doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = Doctor(2, "Dr. Johnson", "Neurology")
    patient1 = Patient(1, "John Doe", date(1993, 5, 15), "Hypertension")
    patient2 = Patient(2, "Jane Doe", date(1998, 3, 20), "Asthma")
    appointment1 = Appointment(1, patient1, doctor1, date(2024, 6, 1), datetime(2024, 6, 1, 10, 0).time())
    appointment2 = Appointment(2, patient2, doctor2, date(2024, 6, 1), datetime(2024, 6, 1, 10, 0).time())
    logger.info(f"Created doctor: {doctor1}")
    logger.info(f"Created doctor: {doctor2}")
    logger.info(f"Created patient: {patient1}")
    logger.info(f"Created patient: {patient2}")
    logger.info(f"Created appointment: {appointment1}")
    logger.info(f"Created appointment: {appointment2}")

    logger.info("app run")
""" handle entry point """
if __name__ == "__main__":
    run()

