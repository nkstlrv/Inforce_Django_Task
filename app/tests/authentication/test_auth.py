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
    assert "password" not in data
    assert response.status_code == 201  # created


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )

    client.post("/api/register/", payload)
    response = client.post("/api/login/", payload)
    assert response.status_code == 200


@pytest.mark.django_db
def test_wrong_credentials_login_user():
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )

    client.post("/api/register/", payload)
    
    response = client.post("/api/login/", dict(username="TestUser", password="WrongPassword"))
    assert response.status_code == 401
    
    response = client.post("/api/login/", dict(username="WrongUser", password="TestPassword"))
    assert response.status_code == 401
    
    
@pytest.mark.django_db
def test_not_enough_credentials_login_user():
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )

    client.post("/api/register/", payload)
    
    response = client.post("/api/login/", dict(username="TestUser"))
    assert response.status_code == 400
    
    response = client.post("/api/login/", dict(password="TestPassword"))
    assert response.status_code == 400
    
    
@pytest.mark.django_db
def test_logout_user():
    payload = dict(
        username="TestUser",
        password="TestPassword"
    )

    client.post("/api/register/", payload)
    
    response = client.get("/api/logout/")
    assert response.status_code == 200
  