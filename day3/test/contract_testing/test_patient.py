import sys
import os
import pytest
import csv
from datetime import datetime
# add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)
from src.models.patient import Patient

@pytest.fixture
def initialize_patient():
    """
    initialize patient object
    """
    patient = Patient(1, "John Doe", datetime.strptime("1990-05-15", "%Y-%m-%d").date(), "Flu")
    return patient

def read_patients_from_csv(file_path):
    """
    read patients from csv file
    """
    patients = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dob = datetime.strptime(row['dob'], "%Y-%m-%d").date()
            patients.append((int(row['id']), row['name'], dob, row['ailment']))
    return patients

def test_patient_creation(initialize_patient):
    """
    test patient creation
    """
    patient = initialize_patient
    patient = Patient(1, "John Doe", datetime.strptime("1990-05-15", "%Y-%m-%d").date(), "Flu")
    assert patient.id == 1
    assert patient.name == "John Doe"
    assert patient.dob == datetime.strptime("1990-05-15", "%Y-%m-%d").date()
    assert patient.ailment == "Flu"

@pytest.mark.parametrize("id, name, dob, ailment", read_patients_from_csv('test/patient.csv'))
def test_parameterized_patient_creation(id, name, dob, ailment):
    """
    test parameterized patient creation
    """
    patient = Patient(id, name, dob, ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment


