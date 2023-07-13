import pytest
from django.urls import reverse, reverse_lazy
from tests.conftest import authenticate
from menu.models import Menu
from restaurants.models import Restaurant


# POST tests:
@pytest.mark.django_db
def test_create_menu(authenticate):
    client = authenticate

    restaurant = Restaurant.objects.create(name='R1',
                                           address='S1',
                                           delivery=True,
                                           phone_number='123')

    url = reverse('menu_create')
    data = {
        'restaurant': restaurant.id,
        'day': 1,
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['restaurant'] == restaurant.id
    assert response.data['day'] == 1
    assert response.data['dishes'] == []


@pytest.mark.django_db
def test_failed_create_menu(authenticate):
    client = authenticate

    # Invalid ID
    url = reverse('menu_create')
    data = {
        'restaurant': 1000,
        'day': 1,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400

    # Invalid day
    url = reverse('menu_create')
    data = {
        'restaurant': 1,
        'day': 8,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400


# PUT tests
@pytest.mark.django_db
def test_update_menu(authenticate):
    client = authenticate

    menu = Menu.objects.create(
        restaurant=Restaurant.objects.create(name='R1', address='S1', delivery=True, phone_number='123'),
        day=1
    )

    # Successful update
    url = reverse('menu_update', kwargs={'pk': menu.id})
    data = {
        'restaurant': menu.restaurant.id,
        'day': 2,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['restaurant'] == menu.restaurant.id
    assert response.data['day'] == 2

    # Invalid restaurant ID
    url = reverse('menu_update', kwargs={'pk': menu.id})
    data = {
        'restaurant': 1000,
        'day': 3,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 400

    # Invalid day
    url = reverse('menu_update', kwargs={'pk': menu.id})
    data = {
        'restaurant': menu.restaurant.id,
        'day': 8,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 400

    # Not existing menu ID
    url = reverse('menu_update', kwargs={'pk': 100})  
    data = {
        'restaurant': menu.restaurant.id,
        'day': 4,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 404
    
# DELETE tests:
@pytest.mark.django_db
def test_delete_menu(authenticate):
    client = authenticate

    menu = Menu.objects.create(
        restaurant=Restaurant.objects.create(name='R1', address='S1', delivery=True, phone_number='123'),
        day=1
    )

    # Successful delete
    url = reverse('menu_delete', kwargs={'pk': menu.id})
    response = client.delete(url)
    assert response.status_code == 204

    # Invalid object to delete
    url = reverse('menu_delete', kwargs={'pk': 10000}) 
    response = client.delete(url)
    assert response.status_code == 404
    
    
# GET tests:
@pytest.mark.django_db
def test_list_menus(authenticate):
    client = authenticate

    menu_1 = Menu.objects.create(
        restaurant=Restaurant.objects.create(name='R1', address='S1', delivery=True, phone_number='123'),
        day=1
    )
    menu_2 = Menu.objects.create(
        restaurant=Restaurant.objects.create(name='R2', address='S2', delivery=False, phone_number='321'),
        day=2
    )

    # Successful list of all menus
    url = reverse('menu_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2

    # Filter by restaurant's ID
    url = reverse('menu_list') + '?restaurant_id=' + str(menu_1.restaurant.id)
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == menu_1.id

    # Filter by day
    url = reverse('menu_list') + '?day=2'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == menu_2.id

    # Filter by restaurant ID and day
    url = reverse('menu_list') + '?restaurant_id=' + str(menu_1.restaurant.id) + '&day=1'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == menu_1.id

    # Filter menus by invalid restaurant ID
    url = reverse('menu_list') + '?restaurant_id=999'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 0

    # Filter menus by invalid day
    url = reverse('menu_list') + '?day=8'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 0
