from rest_framework import serializers
from .models import Restaurant, Menu, Dish, Vote


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
            'id',
            'restaurant',
            'day',
            'dishes',
        )


class DishSerializer(serializers.ModelSerializer):
    """
    Serializer for Dish model
    """
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
        )
        
        
class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Dish model
    """
    class Meta:
        model = Vote
        fields = (
            'id',
            'employee',
            'menu',
        )
