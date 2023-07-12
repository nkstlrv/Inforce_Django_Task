from rest_framework import generics
from .models import Dish
from .serializers import DishSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class DishListAPIView(generics.ListAPIView):
    """
    List all Dishes in DB
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Dish.objects.all()
        _id = self.request.query_params.get('id')

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class DishCreateAPIView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]


class DishUpdateAPIView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]


class DishDeleteAPIView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]
