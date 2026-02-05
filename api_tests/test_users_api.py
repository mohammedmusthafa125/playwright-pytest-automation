import requests

def test_get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_user():
    payload={
        "name":"mustafa",
        "username":"mustafa123",
        "email":"musthafa@test.com"

    }


    response = requests.post("https://jsonplaceholder.typicode.com/users",
                             json = payload)
    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "mustafa"
    assert data["username"] == "mustafa123"
    assert data["email"] == "musthafa@test.com"

