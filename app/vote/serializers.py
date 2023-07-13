from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Vote model
    """
    class Meta:
        model = Vote
        fields = (
            'id',
            'employee',
            'menu',
        )
