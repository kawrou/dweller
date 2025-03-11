import pytest

@pytest.fixture
def normal_user():  
    return {
        'email': "normal@user.com",
        'password': "foo",
        'first_name': "John",
        'last_name': "Doe",
        'dob': "1990-01-01"
    }
