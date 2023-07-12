import pytest
from django.urls import reverse, reverse_lazy
from tests.conftest import authenticate
from restaurants.models import Restaurant


# POST tests:
@pytest.mark.django_db
def test_create_restaurant(authenticate):
    client = authenticate

    url = reverse('restaurant_create')
    data = {
        'name': 'R1',
        'address': 'S1',
        'delivery': True,
        'phone_number': '123'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['name'] == 'R1'
    assert response.data['address'] == 'S1'
    assert response.data['delivery'] == True
    assert response.data['phone_number'] == '123'


@pytest.mark.django_db
def test_filed_create_restaurant(authenticate):
    client = authenticate

    # Empty payload
    url = reverse('restaurant_create')
    payload = {}
    response = client.post(url, payload, format='json')
    assert response.status_code == 400

    # Invalid data
    payload = {
        'name': 'R1',
        'address': 'S1',
        'delivery': 255,
        'phone_number': '123'
    }

    response = client.post(url, payload, format='json')
    assert response.status_code == 400

    # Missing required data
    payload = {
        'address': 'S1',
        'delivery': True,
        'phone_number': '123'
    }

    response = client.post(url, payload, format='json')
    assert response.status_code == 400
    
    
# PUT tests:
@pytest.mark.django_db
def test_update_restaurant(authenticate):
    client = authenticate

    # Test data
    restaurant = Restaurant.objects.create(name='R1', 
                                           address='S1', 
                                           delivery=False,
                                           phone_number='123')

    # Invalid ID
    url = reverse('restaurant_update', kwargs={'pk': 1000})
    data = {
        'name': 'R1 edited',
        'address': 'S1 Edited',
        'delivery': True,
        'phone_number': '321'
    }

    response = client.put(url, data, format='json')
    assert response.status_code == 404

    # Successful update
    url = reverse('restaurant_update', kwargs={'pk': restaurant.pk})
    data = {
        'name': 'R1 edited',
        'address': 'S1 Edited',
        'delivery': True,
        'phone_number': '321'
    }

    response = client.put(url, data, format='json')

    assert response.status_code == 200
    assert response.data['name'] == 'R1 edited'
    assert response.data['address'] == 'S1 Edited'
    assert response.data['delivery'] == True
    assert response.data['phone_number'] == '321'


# DELETE tests:
@pytest.mark.django_db
def test_delete_restaurant(authenticate):
    client = authenticate

    restaurant = Restaurant.objects.create(name='R1', 
                                           address='S1', 
                                           delivery=True,
                                           phone_number='123')

    # Successful delete
    url = reverse('restaurant_delete', kwargs={'pk': restaurant.pk})

    response = client.delete(url)
    assert response.status_code == 204
    assert Restaurant.objects.filter(pk=restaurant.pk).exists() == False
    
    
@pytest.mark.django_db
def test_failed_delete_restaurant(authenticate):
    client = authenticate

    restaurant = Restaurant.objects.create(name='R1', 
                                           address='S1', 
                                           delivery=True,
                                           phone_number='123')

    # Invalid ID
    url = reverse('restaurant_delete', kwargs={'pk': 1000})

    response = client.delete(url)
    assert response.status_code == 404
    assert Restaurant.objects.filter(pk=restaurant.pk).exists() == True


# GET tests:
@pytest.mark.django_db
def test_list_restaurants(authenticate):
    client = authenticate

    r_1 = Restaurant.objects.create(name='R1', 
                                    address='S1', 
                                    delivery=True,
                                    phone_number='123')
    
    r_2 = Restaurant.objects.create(name='R2', 
                                    address='S2', 
                                    delivery=False,
                                    phone_number='321')

    url = reverse('restaurant_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2

    # Successful queried
    url = reverse('restaurant_list') + '?delivery=True'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1 
    assert response.data[0]['name'] == 'R1'
    
    # Invalid ID
    url = reverse('restaurant_list') + '?id=10000'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 0 
    
    # Invalid query
    url = reverse('restaurant_list') + '?invalid_parameter=test'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2 
    assert response.data[0]['name'] == 'R1'
    assert response.data[1]['name'] == 'R2'