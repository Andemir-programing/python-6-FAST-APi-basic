import requests

from tests.configuration import url


class EmployeeClient:
    def __init__(self):
        self.url = url

    @staticmethod
    def print_result(response: requests.Response):
        print("REQUEST INFO")
        print("URL", response.request.url)
        print("BODY", response.request.body)

        print("RESPONSE INFO")
        print("STATUS_CODE", response.status_code)
        print("TEXT", response.text)

    def get_employees(self):
        endpoint = f"{self.url}/employees"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def get_employee_by_id(self, employee_id: int):
        endpoint = f"{self.url}/employee/{employee_id}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def create_employee(self, employee_name, role):
        endpoint = f"{self.url}/employee"
        req_dict = {
            "employee_name": employee_name,
            "role": role
        }

        response = requests.post(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def update_employee(self):
        pass

    def delete_employee(self):
        pass