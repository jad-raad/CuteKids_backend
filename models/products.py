from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from typing import Dict

class Product(): 

    class Products(BaseModel):
        id:UUID
        name:Optional[str] 
        price:Optional[float]
        image:Optional[bytes] 
        description:Optional[str] 
        sizes:Optional[dict] 
        flag:str
        
    class Checkout(BaseModel):
        prod_Id:list
        user_Id:UUID
        price:float

    class RedeemCode(BaseModel):
        code:UUID
        discout:float



    

    
