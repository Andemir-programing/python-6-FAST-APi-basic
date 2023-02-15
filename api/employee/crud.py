"""
Create
Read
Update
Delete
"""
from typing import Type
from fastapi import HTTPException

from api.employee.schemas import EmployeeIn, EmployeeOut, Employee
from db import db_employee, db_token


class Employee:
    def __init__(self, db_session):
        self.db_session = db_session

    def check_token(self, token):
        if not isinstance(token, str):
            return {"message": "incorrect token", "details": "type is not string"}
        if not len(token.split('-')) == 5:
            return {"message": "incorrect token", "details": "token not with 5 blocks"}
        user = db_token.get_user_by_token(self.db_session, token)
        if user is None:
            return {"message": "Authorization error", "details": "token not in cache"}

    def create_employee(self, user_in: EmployeeIn) -> Employee:
        employee = db_employee.create_employee(self.db_session, **user_in.dict())
        user_out = Employee(id=employee.id, name=employee.name,
                            role=employee.role)
        db_token.add_token(self.db_session, user_out.id, user_out.token)
        return user_out

    def get_employee_by_id(self, employee_id: int, token: str):
        errors = self.check_token(token)
        if errors is None:
            employee = db_employee.get_employee_by_id(self.db_session, employee_id)
            if employee:  # ==  if user is not None
                return EmployeeOut(id=employee.id, name=employee.name,
                                   role=employee.role)
            else:
                raise HTTPException(status_code=404, detail={"message": "employee not found!"})
        else:
            raise HTTPException(status_code=400, detail=errors)

    def get_employees(self) -> [EmployeeOut]:
        results = db_employee.get_all_employees(self.db_session)
        employee_outs = []
        for u in results:
            uo = EmployeeOut(id=u.id, name=u.name,role=u.role)
            employee_outs.append(uo)
        return employee_outs

    def put_employee(self, employee_id: int, employee_in: EmployeeIn) -> EmployeeOut:
        employee = db_employee.update_employee(self.db_session, employee_id, employee_in)
        if employee:
            return EmployeeOut(id=employee.id, name=employee.name,
                               role=employee.role)
        else:
            raise HTTPException(status_code=404, detail={"message": "employee not found!"})

    def delete_employee(self, employee_id: int) -> None:
        if not db_employee.delete_employee(self.db_session, employee_id):
            raise HTTPException(status_code=404, detail={"message": "employee not found!"})