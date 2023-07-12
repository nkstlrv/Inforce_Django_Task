import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.fixture
def authenticate_user():
    """
    With this fixture we can easily authenticate before testing endpoints
    """
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )

    client.post("/api/register/", payload)
    client.post("/api/login/", payload)
