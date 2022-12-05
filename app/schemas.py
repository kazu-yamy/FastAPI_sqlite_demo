from pydantic import BaseModel

class ItemBase(BaseModel):
    date: str
    time: str
    temp: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    device_id: int
    owner_id: int
    
    class Config(BaseModel):
        orm_mode = True

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item]
    
    class Config:
        orm_mode = True

