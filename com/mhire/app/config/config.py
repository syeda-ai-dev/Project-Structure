import os
from dotenv import load_dotenv
            
load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.api_key = os.getenv("API_KEY")
            cls._instance.model_name = os.getenv("MODEL")

        return cls._instance