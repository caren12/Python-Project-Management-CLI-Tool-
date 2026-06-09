from models.user import User

def test_user_creation():
    user = User("Alex", "alex@mail.com")
    assert user.name == "Alex"
    assert user.email == "alex@mail.com"