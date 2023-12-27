from pydantic import BaseModel

class Auth(): 

    class SignIn(BaseModel):
        mail:str
        password:str