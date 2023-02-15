from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, Field, validator


class RoleEnum(str, Enum):
    admin = "admin"
    seller = "phones"
    expert = "expert"


class Employee(BaseModel):
    id: int
    name: str
    role: RoleEnum

    # @validator("catalog")
    # def check_catalog(cls, value):
    #     if value not in ["Food", "Furniture", "Vehicle"]:
    #         raise ValueError(f"{value} is not catalog")
    #
    #     return value


class EmployeeBase(BaseModel):
    name: str = None
    id: int = None
    address: str = None
    role: RoleEnum = None


class EmployeeIn(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int


def generate_token():
    return str(uuid4())


class CreateEmployee(EmployeeBase):
    id: int
    token: str = Field(default_factory=generate_token)