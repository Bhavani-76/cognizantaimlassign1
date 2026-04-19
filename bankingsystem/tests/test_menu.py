from src.models.menu import Menu
from src.models.individual import Individual

def test_add_customer():
    menu = Menu()

    customer = Individual("101", "Prerana", "Karnataka", "99999",
                          "mail@gmail.com", "1234",
                          "Umadi", "Female", "30-04-2004")

    menu.add_customer(customer)

    assert len(menu.customer_list) == 1