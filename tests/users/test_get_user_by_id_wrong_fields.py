import pytest


@pytest.mark.parametrize("user_id, exp_code", [
    ([1, 2, 3], 422),
    (None, 422),
    ({4}, 422),
    ({"5"}, 422)
])
def test_negative(user_fixture, user_id, exp_code):
    response = user_fixture.api_client.user.get_user_by_id(user_id)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"