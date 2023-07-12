from rest_framework import generics
from .models import Restaurant, Menu, Dish
from.serializers import RestaurantSerializer


class RestaurantListAPIView(generics.ListAPIView):
    """
    List API view of restaurant model
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer