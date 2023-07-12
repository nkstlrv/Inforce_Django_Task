from django.urls import path
from . import views

urlpatterns = [

    # endpoint for list of all restaurants
    path('restaurants/list/', views.RestaurantListAPIView.as_view(), name='restaurants_list'),

    # endpoint for list of menus. If query parameters are provided, request is being filtered
     path('menus/list/', views.MenuListAPIView.as_view(), name='menus_list'),
    
    # endpoint for list of all dishes
    path('dishes/list/', views.DishListAPIView.as_view(), name='dishes_list'),

]
