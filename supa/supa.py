import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

class Supabase():
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.supabase = create_client(self.url, self.key)

    def login(self, email, password):
        #here you can create different methods for authentication/ data selection/ updating and call them in main.py
        return self.supabase.options()