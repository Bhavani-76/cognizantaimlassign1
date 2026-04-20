import os
from dotenv import load_dotenv
load_dotenv()

class Config():
    def __init__(self):
        self.app_env: str = os.getenv("APP_ENV")
        print(f"App Environment: {self.app_env}")
        self.resource_path: str = self.get_resource_path()

    def get_resource_path(self) -> str:
        if self.app_env == "Production":
           return f"src/resources/customer.json"
        elif self.app_env == "Development":
            return f"src/resources/customer.csv"
        elif self.app_env == "Testing":
            return f"src/resources/customer.txt"
        else:
            raise ValueError("Invalid environment specified. Please set APP_ENV to 'Production', 'Development', or 'Testing'.")
