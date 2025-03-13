import pytest
from datetime import date, timedelta

@pytest.fixture
def normal_user():
    return {
        'email': "user1@user.com",
        'password': 'StrongPassword123',
        'first_name': 'John',
        'last_name': 'Doe',
        'dob': '1990-08-01'
    }

@pytest.fixture
def valid_form_data():
    return {
        'email': "normal@user.com",
        'first_name': "John",
        'last_name': "Doe",
        'date_of_birth': "1990-01-01",
        'password1': "StrongPassword123!",
        'password2': "StrongPassword123!",
    }

@pytest.fixture
def invalid_password_not_matched_form_data():
    return {
        'email': "normal@user.com",
        'first_name': "John",
        'last_name': "Doe",
        'date_of_birth': "1990-01-01",
        'password1': "StrongPassword123!",
        'password2': "StrongPassword456!",
    }

@pytest.fixture
def invalid_password_too_short_form_data(): 
    return {
        'email': "normal@user.com",
        'first_name': "John",
        'last_name': "Doe",
        'date_of_birth': "1990-01-01",
        'password1': "foo",
        'password2': "foo",
    }

@pytest.fixture
def invalid_user_not_18_form_data():
    return {
        'email': "normal@user.com",
        'first_name': "John",
        'last_name': "Doe",
        'date_of_birth': date.today() - timedelta(days=365 * 17), 
        'password1': "StrongPassword123!",
        'password2': "StrongPassword123!",
    }

@pytest.fixture
def invalid_missing_first_name_form_data():
    return {
        'email': "normal@user.com",
        'first_name': "",
        'last_name': "Doe",
        'date_of_birth': date.today() - timedelta(days=365 * 17), 
        'password1': "StrongPassword123!",
        'password2': "StrongPassword123!",
    }

@pytest.fixture
def invalid_missing_last_name_form_data():
    return {
        'email': "normal@user.com",
        'first_name': "John",
        'last_name': "",
        'date_of_birth': date.today() - timedelta(days=365 * 17), 
        'password1': "StrongPassword123!",
        'password2': "StrongPassword123!",
    }
