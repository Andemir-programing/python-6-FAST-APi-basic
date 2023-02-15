from typing import Optional

from db.models import Employee


def get_employee_by_id(db_session, employee_id) -> Optional[Employee]:
    return db_session.query(Employee).filter_by(id=employee_id).first()  # for unique field


def get_employees_by_name(db_session, name) -> list:
    return db_session.query(Employee).filter_by(name=name).all()  # for not unique field


def get_all_employees(db_session):
    employees = db_session.query(Employee).all()  # READ
    return employees


def create_employee(db_session, name=None,role=None):
    employee = Employee(name=name, id=id, role=role)
    db_session.add(employee)  # CREATE
    db_session.commit()
    db_session.refresh(employee)  # refresh, add id to employee
    return employee


def update_employee(db_session, employee_id, new_employee):
    old_employee = get_employee_by_id(db_session, employee_id)  # UPDATE
    if old_employee is not None:
        old_employee.name = new_employee.name if new_employee.name is not None else old_employee.name
        old_employee.age = new_employee.age if new_employee.age is not None else old_employee.age
        old_employee.address = new_employee.address if new_employee.address is not None else old_employee.address
        old_employee.accessed_catalog = new_employee.accessed_catalog if new_employee.accessed_catalog is not None else old_employee.accessed_catalog
        db_session.commit()
        db_session.refresh(old_employee)
        return old_employee


def delete_employee(db_session, employee_id: int):
    employee = get_employee_by_id(db_session, employee_id)
    if employee:
        db_session.delete(employee)  # DELETE
        db_session.commit()
        return True
    else:
        return False