class HealthView:
    @staticmethod
    def display_doctors(doctors):
        print("\n--- Doctors ---")
        for doctor in doctors:
            print(f"Doctor: {doctor.name}, Specialization: {doctor.specialization}")

    @staticmethod
    def display_patients(patients):
        print("\n--- Patients ---")
        for patient in patients:
            print(f"Patient: {patient.name}, Disease: {patient.disease}")

    @staticmethod
    def display_mapping(mapping):
        print("\n--- Patient to Doctor Mapping ---")
        for patient, doctor in mapping.items():
            print(f"{patient} → {doctor}")
