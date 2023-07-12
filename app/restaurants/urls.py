from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint for list of all restaurants
    path('restaurant/list/', views.RestaurantListAPIView.as_view(), name='restaurant_list'),

    # GET endpoint for list of menus. If query parameters are provided, request is being filtered
     path('menu/list/', views.MenuListAPIView.as_view(), name='menu_list'),
    
    # GET endpoint for list of all dishes
    path('dish/list/', views.DishListAPIView.as_view(), name='dish_list'),
    
    # POST endpoint to create new restaurant
    path('restaurant/create/', views.RestaurantCreateAPIView.as_view(), name='restaurant_create'),
    
    # POST endpoint to create new menu
    path('menu/create/', views.MenuCreateAPIView.as_view(), name='menu_create'),
    
    # POST endpoint to create new dish
    path('dish/create/', views.DishCreateAPIView.as_view(), name='dish_create'),
    
    # PUT endpoint to update restaurant
    path('restaurant/update/<int:pk>/', views.RestaurantUpdateAPIView.as_view(), name='restaurant_update'),
    
    # PUT endpoint to update menu
    path('menu/update/<int:pk>/', views.MenuUpdateAPIView.as_view(), name='menu_update'),
    
    # PUT endpoint to update dish
    path('dish/update/<int:pk>/', views.DishUpdateAPIView.as_view(), name='dish_update'),
    
    # DELETE endpoint for restaurant
    path('restaurant/delete/<int:pk>/', views.RestaurantDeleteAPIView.as_view(), name='restaurant_delete'),
    
    # DELETE endpoint for menu
    path('menu/delete/<int:pk>/', views.MenuDeleteAPIView.as_view(), name='menu_delete'),
    
    # DELETE endpoint for dish
    path('dish/delete/<int:pk>/', views.DishDeleteAPIView.as_view(), name='dish_delete'),
    
    # GET endpoint for list of votes
     path('vote/list/', views.VoteListAPIView.as_view(), name='vote_list'),
     
     # POST endpoint to vote
    path('vote/create/', views.VoteCreateAPIView.as_view(), name='vote_create'),
    
    path('vote/delete/<int:pk>/', views.VoteDeleteAPIView.as_view(), name='vote_delete'),
    path('vote/update/<int:pk>/', views.VoteUpdateAPIView.as_view(), name='vote_update'),
    

]
