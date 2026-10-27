from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    email: EmailStr
    password: str
    
class NewUser(User):
    pass

class UserSignIn(BaseModel):
    email: EmailStr
    password: str