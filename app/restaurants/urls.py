from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint | query parameters available
    path('list/', views.RestaurantListAPIView.as_view(), name='restaurant_list'),

    # POST endpoint 
    path('create/', views.RestaurantCreateAPIView.as_view(), name='restaurant_create'),

    # PUT endpoint 
    path('update/<int:pk>/', views.RestaurantUpdateAPIView.as_view(), name='restaurant_update'),

    # DELETE endpoint 
    path('delete/<int:pk>/', views.RestaurantDeleteAPIView.as_view(), name='restaurant_delete'),

]
