from rest_framework import generics
from .models import Restaurant, Menu, Dish
from.serializers import RestaurantSerializer, MenuSerializer


class RestaurantListAPIView(generics.ListAPIView):
    """
    List API view of Restaurant model
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    
class MenuListAPIView(generics.ListAPIView):
    """
    List API view of Menu model
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer