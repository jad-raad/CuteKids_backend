import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

class Supabase():
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.supabase = create_client(self.url, self.key)

    def refresh_session(self, token):
        res = {}
        res["session"] = self.supabase.auth.get_user(token)
        res["user"] = self.supabase.table("users").select("*").match({"id": res["session"].user.id}).execute().data[0]
        if res["user"]["is_admin"] == True:
            res["orders"] = self.supabase.table("orders").select("*").execute().data
        return res

    def login(self, email, password):
        #here you can create different methods for authentication/ data selection/ updating and call them in main.py
        data = {}
        data["session"] = self.supabase.auth.sign_in_with_password({"email": email, "password": password})
        data["user"] = self.supabase.table("users").select("*").match({"id": data["session"].user.id}).execute().data[0]
        if data["user"]["is_admin"] == True:
            data["orders"] = self.supabase.table("orders").select("*").execute().data
        return data

    def signup(self, email, password, name):
        res = self.supabase.auth.sign_up({"email": email, "password": password})
        id = res.user.id
        self.supabase.table("users").insert({"name": name,"id": id}).execute()
        return res  

    def getProducts(self):
        res = self.supabase.table("products").select("*, category(*)").execute()
        return res.data
        
    
    def checkout(self, user_id, products, price, address, district):
        res = self.supabase.table("orders").insert({"user_id": user_id, "products": products, "price": price, "address": address, "district": district}).execute()
        return res 
    