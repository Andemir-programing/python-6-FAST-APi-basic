from pydantic import BaseModel, Field, validator
from typing import List

class Catalog(BaseModel):
    name: str
    catalog: str

    @validator("catalog")
    def check_catalog(cls, value):
        if len(value) > 9:
            raise ValueError("Catalog must be less than 9 symbols")
        if value not in ["Food", "Furniture", "Vehicle"]:
            raise ValueError(f"{value} is not catalog")

        return value

class UserBase(BaseModel):
    user_name: str
    age: int
    address: str
    Accesed_catalog: Catalog = None


class UserIn(UserBase):
    pass


class UserInPut(UserBase):
    user_name: str = None
    age: int = None


class UserOut(UserBase):
    id: int


