import pytest
from django.urls import reverse, reverse_lazy
from tests.conftest import authenticate
from dish.models import Dish


# POST (Create) endpoint tests:
@pytest.mark.django_db
def test_create_successful_dish(authenticate):
    client = authenticate
    url = reverse('dish_create')

    payload = {
        'name': 'test_dish'
    }

    response = client.post(url, payload, format='json')

    assert response.status_code == 201
    assert response.data['name'] == 'test_dish'
    assert 'id' in response.data


@pytest.mark.django_db
def test_create_failed_dish(authenticate):
    client = authenticate
    url = reverse('dish_create')

    payload = {}

    # Empty payload
    response = client.post(url, payload, format='json')
    assert response.status_code == 400

    # invalid data
    payload = {'name': [1, 2, 3]}
    response = client.post(url, payload, format='json')
    assert response.status_code == 400

    # not authenticated user
    client.credentials()
    payload = {'name': 'test_dish'}
    response = client.post(url, payload, format='json')
    assert response.status_code == 401
    assert 'detail' in response.data


# PUT (Update) endpoint tests:
@pytest.mark.django_db
def test_update_dish(authenticate):
    client = authenticate
    dish = Dish.objects.create(name='test_dish')

    url = reverse_lazy('dish_update', kwargs={'pk': dish.pk})
    payload = {'name': 'test_dish'}

    response = client.put(url, payload, format='json')

    assert response.status_code == 200
    assert response.data['name'] == 'test_dish'


@pytest.mark.django_db
def test_failed_update_dish(authenticate):

    client = authenticate
    dish = Dish.objects.create(name='test_dish')

    # No payload
    payload = {}
    url = reverse('dish_update', kwargs={'pk': dish.id})
    response = client.put(url, payload, format='json')
    assert response.status_code == 400

    # Wrong data type
    payload = {
        'name': [1, 2, 3]
    }
    url = reverse('dish_update', kwargs={'pk': dish.id})
    response = client.put(url, payload, format='json')
    assert response.status_code == 400
    
    # Wrong fields
    payload = {
        'field': "test_dish"
    }
    url = reverse('dish_update', kwargs={'pk': dish.id})
    response = client.put(url, payload, format='json')
    assert response.status_code == 400


# DELETE tests:
@pytest.mark.django_db
def test_delete_dish(authenticate):
    
    client = authenticate
    dish = Dish.objects.create(name='test_dish')

    url = reverse('dish_delete', kwargs={'pk': dish.id})
    response = client.delete(url)

    assert response.status_code == 204
    assert Dish.objects.filter(id=dish.id).exists() == False


@pytest.mark.django_db
def test_failed_delete_dish(authenticate):
    client = authenticate

    # Invalid ID
    invalid_dish_id = 10000
    url = reverse('dish_delete', kwargs={'pk': invalid_dish_id})
    response = client.delete(url)
    assert response.status_code == 404
    
    
# GET tests
@pytest.mark.django_db
def test_list_dishes(authenticate):
    client = authenticate

    dish_1 = Dish.objects.create(name='test_dish_1')
    dish_2 = Dish.objects.create(name='test_dish_2')
    
    url = reverse('dish_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['name'] == dish_1.name
    assert response.data[1]['name'] == dish_2.name
    
