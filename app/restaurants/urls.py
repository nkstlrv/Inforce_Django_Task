from django.urls import path
from . import views

urlpatterns = [
    
    # list of restaurants endpoint
    path('list/restaurants/', views.RestaurantListAPIView.as_view(), name='restaurants_list'),
]
