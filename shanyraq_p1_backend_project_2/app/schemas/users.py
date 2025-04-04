from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: EmailStr
    phone: str
    password: str
    name: str
    city: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: EmailStr = None
    phone: str = None
    password: str = None
    name: str = None
    city: str = None
