import json
import pytest


@pytest.mark.gen_test
def test_user_handler_returns_all_users_when_user_id_not_supplied(
    engine_with_schema_and_multiple_users,
    http_client,
    base_url
):
    url = f"{base_url}/api/v1/user"
    response = yield http_client.fetch(url)
    assert response.code == 200
    body = json.loads(response.body)
    assert len(body["users"]) == 3
    assert body['users'][0]['first_name'] == "Tony"

