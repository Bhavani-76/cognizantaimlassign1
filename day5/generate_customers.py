import csv
from faker import Faker

fake = Faker()

# Create CSV file
with open('customers.csv', 'w', newline='') as csvfile:
    fieldnames = ['customer_id', 'first_name', 'last_name', 'email', 'phone_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(1, 11):  # 10 customers
        writer.writerow({
            'customer_id': i,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number()
        })

print("customers.csv created with 10 fake customers.")