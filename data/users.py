def users():
    return {
        "users": [
            {
                "username": "alice",
                "id": "1",
            },
            {
                "username": "bob",
                "id": "2",
            },
        ]
    }


def get_username(username) -> (list, str):
    user_db = users()["users"]
    for user in user_db:
        if username == user["username"]:
            return user["username"]
    return None

def get_user_id(username) -> (list, str):
    user_db = users()["users"]
    for user in user_db:
        if username == user["username"]:
            return user["id"]
    return None