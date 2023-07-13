import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def authenticate():
    """
    Fixture to login user before testing endpoints
    """
    client = APIClient()

    user = User.objects.create_user(username='test_user', password='test_password')
    client.post('/api/register/', {'username': 'test_user', 'password': 'test_password'})

    response = client.post('/api/login/', {'username': 'test_user', 'password': 'test_password'})
    access_token = response.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    return client
