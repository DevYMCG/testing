from pydantic import BaseModel, EmailStr


class Users(BaseModel):
    email:EmailStr
    password: str