from rest_framework import serializers
from .models import Restaurant, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializer for Restaurant model
    """
    class Meta:
        model = Restaurant
        fields = (
            '__all__'
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
