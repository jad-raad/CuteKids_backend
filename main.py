from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import supabase
from supa.supa import Supabase
from  models.auth import Auth
from  models.products import Product
from dotenv import load_dotenv
from os import environ as env
import uvicorn
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello world"}
 
@app.post("/signup")
def signup(User:Auth().SignUp):
    return Supabase().signup(User.email, User.password, User.name)

@app.post("/login")
def login(User:Auth().Login):
    return Supabase().login(User.email, User.password)

@app.get("/refresh_session")
def register(token: str):
    return Supabase().refresh_session(token)

@app.get("/get_products")
def getProducts():
    return Supabase().getProducts()

@app.post("/add_product")
def addProduct(Product: Product().AddProduct):
    return True

@app.post("/checkout")
def checkout(Product:Product().Checkout):
    return Supabase().checkout(Product.user_id, Product.products, Product.price, Product.address, Product.district)

@app.post("/redeemCode")
def redeemCode(Product:Product().RedeemCode):
    return Supabase().RedeemCode()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=9514)