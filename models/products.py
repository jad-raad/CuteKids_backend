from pydantic import BaseModel

class Product(): 

    class AddProduct(BaseModel):
        name:str
        price:float
        image:bytes
        description:str
        sizes:dict