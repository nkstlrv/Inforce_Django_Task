from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class VoteListAPIView(generics.ListAPIView):
    """
    Returns all Votes
    Also can be filtered by ID query parameters:
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        queryset = Vote.objects.all()
        _id = self.request.query_params.get('id')

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class VoteCreateAPIView(generics.CreateAPIView):
    """
    Creation method view to be used by POST API endpoint
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class VoteDeleteAPIView(generics.DestroyAPIView):
    """
    Deletion method view to be used by DELETE API endpoint
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class VoteUpdateAPIView(generics.UpdateAPIView):
    """
    Instance editing method view to be used by PUT/PATCH API endpoint
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]
