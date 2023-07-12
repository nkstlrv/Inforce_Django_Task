from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint for list of all restaurants
    path('list/', views.RestaurantListAPIView.as_view(), name='restaurant_list'),


    # POST endpoint to create new restaurant
    path('create/', views.RestaurantCreateAPIView.as_view(), name='restaurant_create'),


    # PUT endpoint to update restaurant
    path('update/<int:pk>/', views.RestaurantUpdateAPIView.as_view(), name='restaurant_update'),


    # DELETE endpoint for restaurant
    path('delete/<int:pk>/', views.RestaurantDeleteAPIView.as_view(), name='restaurant_delete'),


    # GET endpoint for list of votes
    path('vote/list/', views.VoteListAPIView.as_view(), name='vote_list'),

    # POST endpoint to vote
    path('vote/create/', views.VoteCreateAPIView.as_view(), name='vote_create'),

    path('vote/delete/<int:pk>/', views.VoteDeleteAPIView.as_view(), name='vote_delete'),
    path('vote/update/<int:pk>/', views.VoteUpdateAPIView.as_view(), name='vote_update'),


]
