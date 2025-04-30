import pytest
# from tests.utils import create_user
# from src.core.base.token import JWTToken


@pytest.mark.asyncio(loop_scope="session")
async def test_users_list_empty_success(client):
    # user = await create_user()
    # payload = {"sub": user.username, "user_id": str(user.id)}
    # tokens = JWTToken.tokens(payload=payload)

    response = await client.get(
        "/api/v1/users",
        # headers={"Authorization": f'Bearer {tokens['access']}'},
    )

    # response_data = response.json()

    # user_data = response_data["user"]
    ######### assert response ##########
    assert response.status_code == 200
    # assert user_data["id"] == str(user.id)
    # assert user_data["tid"] == user.tid
    # assert user_data["first_name"] == user.first_name
    # assert user_data["last_name"] == user.last_name
    # assert user_data["username"] == user.username
    # assert user_data["is_bot"] == user.is_bot
    # assert user_data["created_at"] == user.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    ####################################
