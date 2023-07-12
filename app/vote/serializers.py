from rest_framework import serializers
from .models import Vote


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
