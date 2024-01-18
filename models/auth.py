from pydantic import BaseModel

class Auth(): 

    class SignUp(BaseModel):
        email:str
        password:str
        name:str

    class Login(BaseModel):
        email:str
        password:str
