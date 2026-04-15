from faker import Faker
import random
from module.doctor import Doctor
from module.patient import Patient

class HealthStore:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.fake = Faker()

    def generate_doctors(self, count=3):
        specializations = ["Cardiology", "Neurology", "Dermatology", "Orthopedics", "Psychiatry"]
        for _ in range(count):
            name = self.fake.name()
            specialization = random.choice(specializations)
            self.doctors.append(Doctor(name, specialization))

    def generate_patients(self, count=5):
        diseases = {
            "Cardiology": ["Heart Disease", "Arrhythmia"],
            "Neurology": ["Migraine", "Epilepsy"],
            "Dermatology": ["Skin Rash", "Eczema"],
            "Orthopedics": ["Fracture", "Arthritis"],
            "Psychiatry": ["Depression", "Anxiety"]
        }
        for _ in range(count):
            name = self.fake.name()
            specialization = random.choice(list(diseases.keys()))
            disease = random.choice(diseases[specialization])
            self.patients.append(Patient(name, disease))

    def map_patient_to_doctor(self):
        mapping = {}
        for patient in self.patients:
            for doctor in self.doctors:
                if doctor.specialization.lower() in patient.disease.lower() or patient.disease in doctor.specialization:
                    mapping[patient.name] = doctor.name
                    break
            else:
                mapping[patient.name] = "No doctor available"
        return mapping
