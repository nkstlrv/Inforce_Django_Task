from rest_framework import generics
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, DishSerializer


class RestaurantListAPIView(generics.ListAPIView):
    """
    List all Restaurants in DB
    """
    serializer_class = RestaurantSerializer
    
    def get_queryset(self):
        queryset = Restaurant.objects.all()
        restaurant_id = self.request.query_params.get('id')

        if restaurant_id:
            queryset = queryset.filter(id=restaurant_id)

        return queryset


class MenuListAPIView(generics.ListAPIView):
    """
    List all Menus in DB

    Restaurant represents as ID

    Days of the week represents as integer
    0 - menu available every day
    1 - 7 --> Monday - Sunday

    To get all menus by providing specific day there is get_queryset() method
    """
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.objects.all()
        day = self.request.query_params.get('day')
        restaurant_id = self.request.query_params.get('restaurant_id')

        if day:
            queryset = queryset.filter(day=day)
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)

        return queryset


class DishListAPIView(generics.ListAPIView):
    """
    List all Dishes in DB
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None), 
                        phone_number=self.request.data.get('phone_number', None))
