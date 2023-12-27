from fastapi import FastAPI
from supa.supa import Supabase
from  models.auth import Auth
from  models.products import Product

app = FastAPI()

supabase_instance = Supabase()

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.post("/sign-in")
def SignIn(User:Auth().SignIn):
    # Use the pre-created supabase_instance instead of creating a new one
    return supabase_instance.SignIn("test", "test")