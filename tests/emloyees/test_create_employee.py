import random
import string

from tests.clients.clients_bundle import employee_client
from tests.configuration import ROLE_ENUM


def test_positive():
    # precondition - предусловие. Создание данных
    employee_name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    role = {
        "name": "test_" + "".join(random.sample(string.ascii_letters, 5)),
        "role": random.choice(ROLE_ENUM)
    }

    # request execution
    response = employee_client.create_employee(employee_name, role)

    assert response.status_code == 200, "fail"