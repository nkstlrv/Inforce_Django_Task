from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.views import AuthBaseClass


class VoteListAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Vote.objects.all()
        _id = self.request.query_params.get('id')

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class VoteCreateAPIView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class VoteDeleteAPIView(generics.DestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class VoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
