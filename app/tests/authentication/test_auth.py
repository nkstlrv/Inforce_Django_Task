import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_register_user():
    
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )
    
    response = client.post("/api/register/", payload)
    
    data = response.data
    assert data['username'] == payload['username']
    