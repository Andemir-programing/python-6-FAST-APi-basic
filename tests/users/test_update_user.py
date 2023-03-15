import random
import pytest


@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [
    ('Ivan', 12, "Nalchik", {"name": "Andemir", "catalog": "phones"}, 200),
    ("Ivan", 32, "Moscow", {"name": "Volodya", "catalog": "food"}, 200),
    ("Ivan", 4, "Saint Petersburg", {"name": "Ahmed", "catalog": "furniture"}, 200),
    ("Ivan", 5, "Rome", {"name": "Damir", "catalog": "vehicle"}, 200),
    ("Ivan", 28, "Paris", {"name": "Ilyas", "catalog": "international_food"}, 200)
])
def test_positive(user_fixture, new_name, new_role):
    user_id = user_fixture.user_id

    response = user_fixture.api_client.user.update_user(user_id, new_name, new_role)

    resp = user_fixture.api_client.user.get_user_by_id(user_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert user_fixture.checkers.validate_json(response.json(), "schemas/user.json")
    if new_name is not None:
        assert resp.json()["name"] == new_name
    if new_role is not None:
        assert resp.json()["role"] == new_role