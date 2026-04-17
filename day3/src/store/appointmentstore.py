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
class AppointmentStore:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments
    
    def get_all_appointments(self):
        return self.appointments
    def get_appointment_by_id(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")
    def delete_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                self.appointments.remove(appointment)
                return
        raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")
    def update_appointment(self, appointment_id, updated_appointment):
        for index, appointment in enumerate(self.appointments):
            if appointment.appointment_id == appointment_id:
                self.appointments[index] = updated_appointment
                return
        raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")