import pandas as pd
import json
from json import JSONDecodeError
from src.models.customer import Customer
from src.models.full_name import FullName
from src.dataloaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl


class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except JSONDecodeError:
            print(f"Warning: Failed to decode JSON from {file_path}. Skipping this file.")
            return        



        # Read JSON file into a DataFrame
        df = pd.DataFrame(data)

        for _, row in df.iterrows():
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = row['phone_no']

            # Create FullName object
            full_name = FullName(first_name=first_name, last_name=last_name)

            # Create Customer object
            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )

            # Add to store
            customer_store.add_customer(customer)
