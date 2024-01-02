from pydantic import BaseModel

class Auth(): 

    class SignUp(BaseModel):
        email:str
        password:str
        name:str
        phone_number:str

    class Login(BaseModel):
        email:str
        password:str
