#это делаю я
import pytest

@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [
    ('Ivan', 12, "Nalchik", {"name": "Andemir", "catalog": "phones"}, 200),
    ("Ivan", 32, "Moscow", {"name": "Volodya", "catalog": "food"}, 200),
    ("Ivan", 4, "Saint Petersburg", {"name": "Ahmed", "catalog": "furniture"}, 200),
    ("Ivan", 5, "Rome", {"name": "Damir", "catalog": "vehicle"}, 200),
    ("Ivan", 28, "Paris", {"name": "Ilyas", "catalog": "international_food"}, 200)
])
def test_positive(application, username, age, address, accessed_catalog, exp_code):
    response = application.api_client.user.update_user(username, age, address, accessed_catalog)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"