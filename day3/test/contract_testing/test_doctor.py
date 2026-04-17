import sys
import os
import pytest
import csv

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)
from src.models.doctor import Doctor
"""
test for doctor object created
"""
@pytest.fixture
def initialize_doctor():
    """
    initialize doctor object
    """
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    return doctor

def read_doctors_from_csv(file_path):
    """
    read doctors from csv file
    """
    doctors = []
    with open('test/doctors.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctors.append((int(row['id']), row['name'], row['specialization']))
    return doctors

def test_doctor_creation(initialize_doctor):
    """
    test doctor creation
    """

    doctor = initialize_doctor
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialty == "Cardiology"

@pytest.mark.parametrize("id, name, specialty",read_doctors_from_csv('test/doctors.csv'))


def test_parameterized_doctor_creation(id, name, specialty):
    """
    test parameterized doctor creation
    """
    doctor = Doctor(id, name, specialty)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialty == specialty

