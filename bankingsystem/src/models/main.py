from savings_account import SavingsAccount
from current_account import CurrentAccount
from individual import Individual
from corporate import Corporate
from menu import Menu
from abc_banking_group import ABCBankingGroup

# Inheritance
sa = SavingsAccount(10000, "01-01-2025", 5)
ca = CurrentAccount(20000, "01-01-2025", 1000)

# Customer Objects
ind = Individual("101", "Prerana", "Karnataka", "9999999999",
                 "mail@gmail.com", "1234", "Umadi", "Female", "30-04-2004")

corp = Corporate("102", "ABC Ltd", "Bangalore", "8888888888",
                 "abc@gmail.com", "5678", "IT")

# Aggregation
menu = Menu()
menu.add_customer(ind)
menu.add_customer(corp)

# Association
bank = ABCBankingGroup()
bank.add_account(sa)
bank.add_account(ca)

print("Project Executed Successfully")