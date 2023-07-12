from rest_framework import generics
from .models import Restaurant, Menu, Dish
from.serializers import RestaurantSerializer, MenuSerializer, DishSerializer


class RestaurantListAPIView(generics.ListAPIView):
    """
    List API view of Restaurant model
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    
class MenuListAPIView(generics.ListAPIView):
    """
    List API view of Menu model
    
    Restaurant represents as ID
    
    Days of the week represents as integer
    0 - menu available every day
    1 - 7 --> Monday - Sunday
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class DishListAPIView(generics.ListAPIView):
    """
    List API for Dish model
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer