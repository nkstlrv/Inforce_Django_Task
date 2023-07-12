from rest_framework import serializers
from .models import Restaurant, Menu, Dish


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializer for Restaurant model
    """
    class Meta:
        model = Restaurant
        fields = (
            '__all__'
        )


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for Menu model
    """
    class Meta:
        model = Menu
        fields = (
            'restaurant',
            'day',
        )


class DishSerializer(serializers.ModelSerializer):
    """
    Serializer for Dish model
    """
    class Meta:
        model = Dish
        fields = (
            'name',
            'menu',
        )
