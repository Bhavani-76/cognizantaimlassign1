from store.health import HealthStore
from view.healthview import HealthView

def main():
    store = HealthStore()
    store.generate_doctors(count=4)
    store.generate_patients(count=6)

    # Display doctors and patients
    HealthView.display_doctors(store.doctors)
    HealthView.display_patients(store.patients)

    # Display mapping
    mapping = store.map_patient_to_doctor()
    HealthView.display_mapping(mapping)

if __name__ == "__main__":
    main()
