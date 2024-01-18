from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from typing import Dict
from fastapi import UploadFile

class Product(): 

    class Products(BaseModel):
        id:UUID
        name:Optional[str] 
        price:Optional[float]
        image:Optional[bytes] 
        description:Optional[str] 
        sizes:Optional[dict] 
        flag:str

    class AddProduct(BaseModel):
        productName: str
        price: int
        description: str
        sizes: list
        gender: str
        image: UploadFile
        
    class Checkout(BaseModel):
        products:list
        user_id:str
        price:int
        address: str
        district: str

    class RedeemCode(BaseModel):
        code:UUID
        discout:float

    class AddToCard(BaseModel):
        product_id: UUID
        quantity: int
        size: str
        user_id: UUID


    

    
