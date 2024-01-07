from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import supabase
from supa.supa import Supabase
from  models.auth import Auth
from  models.products import Product

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.post("/signup")
def signup(User:Auth().SignUp):
    return Supabase().signup(User.email, User.password, User.name, User.phone_number)

@app.post("/login")
def login(User:Auth().Login):
    return Supabase().login(User.email, User.password)

@app.get("/get_products")
def getProducts():
    return Supabase().getProducts()

@app.post("/checkout")
def checkout(Product:Product().Checkout):
    return Supabase().checkout()

@app.post("/redeemCode")
def redeemCode(Product:Product().RedeemCode):
    return Supabase().RedeemCode()

@app.get("/get_orders")
def getOrders():
    return Supabase().getOrders()

@app.post("/add_products")
def addProducts(Product:Product().AddProducts):
    return Supabase().add_products()

@app.post("/update_delivery_status")
def updateDeliveryStatus(Product:Product().Orders):
    return Supabase().update_delivery_status()