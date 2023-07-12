import pytest
from django.urls import reverse
from tests.conftest import authenticate_user


@pytest.mark.django_db
def test_create_dish(authenticate_user):
    client = authenticate_user
    url = reverse('dish_create')
    
    payload = {
        'name': 'Pizza'
        }

    response = client.post(url, payload, format='json')

    assert response.status_code == 201
    assert response.data['name'] == 'Pizza'
