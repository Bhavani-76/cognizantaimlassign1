from src.models.individual import Individual
from src.models.corporate import Corporate

def test_individual():
    ind = Individual("101", "Prerana", "Karnataka", "99999",
                     "mail@gmail.com", "1234",
                     "Umadi", "Female", "30-04-2004")

    assert ind.name == "Prerana"
    assert ind.gender == "Female"

def test_corporate():
    corp = Corporate("102", "ABC Ltd", "Bangalore", "88888",
                     "abc@gmail.com", "5678", "IT")

    assert corp.name == "ABC Ltd"
    assert corp.company_type == "IT"