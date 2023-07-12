from datetime import date, timedelta
from rest_framework import generics, status
from .models import Restaurant,  Dish, Vote
from .serializers import RestaurantSerializer, DishSerializer, VoteSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication.views import AuthBaseClass
from rest_framework.views import APIView
from django.db.models import Count


class RestaurantListAPIView(AuthBaseClass, generics.ListAPIView):
    """
    List all Restaurants in DB
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        _id = self.request.query_params.get('id')
        delivery = self.request.query_params.get('delivery')

        if _id:
            queryset = queryset.filter(id=_id)

        if delivery:
            queryset = queryset.filter(delivery=delivery)

        return queryset


class DishListAPIView(AuthBaseClass, generics.ListAPIView):
    """
    List all Dishes in DB
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RestaurantCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None),
                        phone_number=self.request.data.get('phone_number', None))


class DishCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantUpdateAPIView(AuthBaseClass, generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishUpdateAPIView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class DishDeleteAPIView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class VoteListAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class VoteCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDeleteAPIView(AuthBaseClass, generics.DestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteUpdateAPIView(AuthBaseClass, generics.UpdateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
