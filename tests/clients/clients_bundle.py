from tests.clients.user import UserClient
from tests.clients.employee import EmployeeClient
from tests.clients.product import ProductClient
from tests.clients.manufacturer import ManufacturerClient


class Client:
    user = UserClient()
    employee = EmployeeClient()
    product = ProductClient()
    manufacturer = ManufacturerClient()


"""
bundle-пакет
собираю в одном файле все объекты классов клиентов
"""