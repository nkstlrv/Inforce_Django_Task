from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint for list of all restaurants
    path('restaurant/list/', views.RestaurantListAPIView.as_view(), name='restaurant_list'),

    # GET endpoint for list of menus. If query parameters are provided, request is being filtered
     path('menu/list/', views.MenuListAPIView.as_view(), name='menu_list'),
    
    # GET endpoint for list of all dishes
    path('dish/list/', views.DishListAPIView.as_view(), name='dish_list'),
    
    #POST endpoint to create new restaurant
    path('restaurant/create/', views.RestaurantCreateAPIView.as_view(), name='restaurant_create'),
    
    #POST endpoint to create new menu
    path('menu/create/', views.MenuCreateAPIView.as_view(), name='menu_create'),
    
    #POST endpoint to create new dish
    path('dish/create/', views.DishCreateAPIView.as_view(), name='dish_create'),

]
