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
        prod_id:list
        user_id:UUID
        price:float

    class RedeemCode(BaseModel):
        code:UUID
        discout:float

    class Orders(BaseModel):
        id:UUID
        user_id:UUID
        prod_id:list
        total_price:float
        delivery_status:bool

    


    

    
