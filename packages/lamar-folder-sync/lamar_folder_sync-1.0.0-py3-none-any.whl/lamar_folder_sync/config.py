import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

API_KEY = os.getenv("LAMAR_API_KEY")

if not API_KEY:
    raise ValueError("API Key not set. Please set the LAMAR_API_KEY environment variable.")