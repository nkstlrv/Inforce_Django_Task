from rest_framework import serializers
from .models import Restaurant, Menu, Dish


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializer for Restaurant model
    """
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'address',
            'phone_number',
            'delivery',
        )
