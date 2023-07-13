from rest_framework import generics
from .serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


# class AuthBaseClass(APIView):
#     permission_classes = [IsAuthenticated]
