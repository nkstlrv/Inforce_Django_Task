from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser
from authentication.views import AuthBaseClass


class VoteListAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Vote.objects.all()
        _id = self.request.query_params.get('id')

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class VoteCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDeleteAPIView(AuthBaseClass, generics.DestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteUpdateAPIView(AuthBaseClass, generics.UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
