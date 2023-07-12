from rest_framework import generics
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, DishSerializer
from authentication.views import AuthAPIView 




class RestaurantListAPIView(generics.ListAPIView, AuthAPIView):
    """
    List all Restaurants in DB
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        _id = self.request.query_params.get('id')
        delivery = self.request.query_params.get('delivery')

        if _id:
            queryset = queryset.filter(id=_id)

        if delivery:
            queryset = queryset.filter(delivery=delivery)

        return queryset


class MenuListAPIView(generics.ListAPIView, AuthAPIView):
    """
    List all Menus in DB

    Restaurant represents as ID

    Days of the week represents as integer
    0 - menu available every day
    1 - 7 --> Monday - Sunday

    To get all menus by providing specific day there is get_queryset() method
    """
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def get_queryset(self):
        queryset = Menu.objects.all()
        day = self.request.query_params.get('day')
        restaurant_id = self.request.query_params.get('restaurant_id')
        _id = self.request.query_params.get('id')

        if day:
            queryset = queryset.filter(day=day)

        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)

        if _id:
            queryset = queryset.filter(id=id)

        return queryset


class DishListAPIView(generics.ListAPIView, AuthAPIView):
    """
    List all Dishes in DB
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantCreateAPIView(generics.CreateAPIView, AuthAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None),
                        phone_number=self.request.data.get('phone_number', None))


class MenuCreateAPIView(generics.CreateAPIView, AuthAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishCreateAPIView(generics.CreateAPIView, AuthAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantUpdateAPIView(generics.UpdateAPIView, AuthAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuUpdateAPIView(generics.UpdateAPIView, AuthAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishUpdateAPIView(generics.UpdateAPIView, AuthAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantDeleteAPIView(generics.DestroyAPIView, AuthAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuDeleteAPIView(generics.DestroyAPIView, AuthAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishDeleteAPIView(generics.DestroyAPIView, AuthAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
