from pydantic import Field
from models.company_type import CompanyType
from models.customer import Customer
class Corporate(Customer):
    company_type: CompanyType = Field(..., description="The type of the company, must be one of Private, Public, or Government")
    registration_number: str = Field(..., pattern="^[A-Z0-9]+$", description="The registration number of the company, must contain only uppercase letters and numbers")
