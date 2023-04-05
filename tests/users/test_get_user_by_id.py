def test_positive(user_fixture):
    user_id = user_fixture.user_id

    response = user_fixture.api_client.user.get_user_by_id(user_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    #assert user_fixture.checkers.validate_json(response.json(), "schemas/user.json")