import pytest
@pytest.fixture(scope="session")

def shared_user():
    return {"username": "paralleluser", "password": "Test123"}

def login(user):
    print(f"logging in with {user['username']} and {user['password']}")

def change_password(user):
    print(f"changing password to {user['username']}")
    user["password"] = "NewPassword123"

def test_login(shared_user):
    login(shared_user)

def test_change_password(shared_user):
    change_password(shared_user)