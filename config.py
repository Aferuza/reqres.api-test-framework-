
import os
from dotenv import load_dotenv

# Find and load the .env file automatically
load_dotenv()

BASE_URL = "https://reqres.in/api"
TIMEOUT = 5

# Read the token from the environment; use a safe fallback string for local runs if empty
REQRES_API_TOKEN = os.getenv("REQRES_API_TOKEN", "fallback_local_mock_token")