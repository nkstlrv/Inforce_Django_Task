from django.urls import path
from . import views

urlpatterns = [

    # endpoint for list of all restaurants
    path('list/restaurants/', views.RestaurantListAPIView.as_view(), name='restaurants_list'),

    # endpoint for list of all menus
    path('list/menus/', views.MenuListAPIView.as_view(), name='menus_list'),

]
