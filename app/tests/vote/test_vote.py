from datetime import date, timedelta
import pytest
from django.urls import reverse
from rest_framework import status
from vote.models import Vote
from menu.models import Menu
from restaurants.models import Restaurant
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import random


# POST tests:
@pytest.mark.django_db
def test_create_vote(authenticate):
    client = authenticate

    menu = Menu.objects.create(day=date.today().weekday())
    username = 'test_user_' + str(random.randint(1, 1000))
    user = User.objects.create_user(username=username, password='test_password')

    # Successful create
    url = reverse('vote_create')
    data = {
        'employee': user.id,
        'menu': menu.id,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['employee'] == user.id
    assert response.data['menu'] == menu.id

    # Invalid menu ID
    url = reverse('vote_create')
    data = {
        'employee': user.id,
        'menu': 1000,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400

    # Missing data
    url = reverse('vote_create')
    data = {
        'employee': user.id,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    
    # Vote for not todays's menu
    today = date.today()
    tomorrow = today + timedelta(days=1)
    
    restaurant = Restaurant.objects.create(name='R1', address='S1', delivery=True, phone_number='123')
    invalid_menu = Menu.objects.create(restaurant=restaurant, day=tomorrow.weekday())
    invalid_data = {'employee': user.id, 'menu': invalid_menu.id}
    response = client.post(url, invalid_data)
    assert response.status_code == 400


# PUT tests:
@pytest.mark.django_db
def test_update_vote(authenticate):
    client = authenticate

    menu = Menu.objects.create(day=date.today().weekday())
    username = 'test_user_' + str(random.randint(1, 1000))
    user = User.objects.create_user(username=username, password='test_password')
    vote = Vote.objects.create(employee=user, menu=menu)

    # Successful update
    url = reverse('vote_update', kwargs={'pk': vote.id})
    data = {
        'employee': user.id,
        'menu': menu.id,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['employee'] == user.id
    assert response.data['menu'] == menu.id

    # Invalid ID
    url = reverse('vote_update', kwargs={'pk': 1000})
    data = {
        'employee': user.id,
        'menu': menu.id,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 404

    # Missing data
    url = reverse('vote_update', kwargs={'pk': vote.id})
    data = {
        'employee': user.id,
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 400


# DELETE tests
@pytest.mark.django_db
def test_delete_vote(authenticate):
    client = authenticate

    menu = Menu.objects.create(day=date.today().weekday())
    username = 'test_user_' + str(random.randint(1, 1000))
    user = User.objects.create_user(username=username, password='test_password')
    vote = Vote.objects.create(employee=user, menu=menu)

    # Successful delete
    url = reverse('vote_delete', kwargs={'pk': vote.id})
    response = client.delete(url)
    assert response.status_code == 204

    # Invalid ID
    url = reverse('vote_delete', kwargs={'pk': 1000})
    response = client.delete(url)
    assert response.status_code == 404
    

# GET tests:
@pytest.mark.django_db
def test_list_votes(authenticate):
    client = authenticate

    user1 = User.objects.create_user(username='user1', password='password1')
    user2 = User.objects.create_user(username='user2', password='password2')

    restaurant1 = Restaurant.objects.create(name='R1', address='S1', delivery=True, phone_number='123')
    restaurant2 = Restaurant.objects.create(name='R2', address='S2', delivery=True, phone_number='321')

    today = date.today()
    menu1 = Menu.objects.create(restaurant=restaurant1, day=today.weekday())
    menu2 = Menu.objects.create(restaurant=restaurant2, day=today.weekday())

    vote1 = Vote.objects.create(employee=user1, menu=menu1)
    vote2 = Vote.objects.create(employee=user2, menu=menu2)

    # List all votes
    url = reverse('vote_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2

    # Test case 2: Filter votes by employee ID
    url = reverse('vote_list') + '?employee_id=' + str(user1.id)
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['employee'] == user1.id

    # Test case 3: Filter votes by non-existing employee ID
    url = reverse('vote_list') + '?employee_id=999'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2

