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
        data = self.supabase.auth.sign_in_with_password({"email": email, "password": password})
        return data
    
    def signup(self, email, password, name, phone_number):
        res = self.supabase.auth.sign_up({"email": email, "password": password})
        id = res.user.id
        self.supabase.table("users").insert({"name": name,"id": id,"phone_number": phone_number}).execute()
        return res
    
    def getProducts(self):
        res = self.supabase.table("products").select("*").execute()
        return res.data
        
    
    def checkout(self, prod_Id, user_Id, price):
        res = self.supabase.table("orders").insert({"prod_Id": prod_Id, "user_Id": user_Id, "price": price}).execute()
        return res
    
    def redeemCode(self, code, discount):
        res = self.supabase.table("promo_codes").insert({"code": code,"discount": discount}).execute()
        return res

    def getOrders(self):
        res = self.supabase.table("orders").select("*").execute()
        return res.data
    
    #ID to be discussed 
    def add_products(self,id,name,price,image,description,sizes,flag):
        res = self.supabase.table("products").insert({"name": name,"price": price,"image": image,"description": description,"sizes": sizes,"flag": flag})

    def update_delivery_status(slef,delivery_status):
        res = self.supabase.table("orders").insert({"delivery_status": delivery_status})
        return res

    
    