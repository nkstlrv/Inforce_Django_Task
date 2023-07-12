from rest_framework import serializers
from .models import Menu


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
