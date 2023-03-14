#это делаю я
import pytest
import string

@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [
    ([1, 2, 3], 12, "grhgn j", {"name": "idk", "catalog": "phones"}, 422),
    ("Ivan", "five", "ffdhnm", {"name": "blabla", "catalog": "phones"}, 422),
    ("Ivan", 4, ['idk'], {"name": "dgreggggih", "catalog": "phones"}, 422),
    ("Ivan", 5, "dfhurieg", ["idk"], 422)
])
def test_negative(application, username, age, address, accessed_catalog, exp_code):
    response = application.api_client.user.update_user(username, age, address, accessed_catalog)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"