import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: EmailStr
    password: str
    register_date: datetime.datetime
    is_active: bool

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=4)
    passwordTwo: str
    is_active: bool = False

    @validator('passwordTwo')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("passwords don't match")
        return v