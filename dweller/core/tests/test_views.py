from django.test import TestCase
import pytest
from django.urls import reverse

# Create your tests here.
@pytest.mark.django_db
def test_home_view_returns_hello_world(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200

    content = response.content.decode('utf-8')
    assert "Hello World" in content
