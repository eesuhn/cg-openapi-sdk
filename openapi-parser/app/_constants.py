import os

from dotenv import load_dotenv


load_dotenv()
SECRET = os.getenv("SECRET")
