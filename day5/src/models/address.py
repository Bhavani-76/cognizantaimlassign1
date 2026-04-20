#create address clas associated with customer and corporate class using pydantic
from pydantic import Field
from models.customer import Customer
class Address(BaseModel):
    customer_id : Customer
    street: str = Field(..., min_length=2, max_length=100, description="street address of the customer")
    city: str = Field(..., min_length=2, max_length=100, description="The city of the customer")
    state: str = Field(..., min_length=2, max_length=100, description="The state of the customer")
    zip_code: str = Field(..., min_length=5, max_length=5, description="The zip code of the customer, must be a 5 digit number")
    country: str = Field(..., min_length=2, max_length=100, description="The country of the customer")