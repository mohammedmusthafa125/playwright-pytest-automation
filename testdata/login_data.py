login_test_data = [
    {
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
        "expected": "success"
    },
    {
        "username": "wrong",
        "password": "wrong",
        "expected": "failure"
    }
]
negative_login_data = [
    {"username": "", "password": "SuperSecretPassword!", "expected": "Your username is invalid!"},
    {"username": "tomsmith", "password": "", "expected": "Your password is invalid!"},
    {"username": "", "password": "", "expected": "Your username is invalid!"},
    {"username": "wrong", "password": "wrong", "expected": "Your username is invalid!"}
]
