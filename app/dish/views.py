from rest_framework import generics
from .models import Dish
from .serializers import DishSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class DishListAPIView(generics.ListAPIView):
    """
    Returns all dishes, used by GET endpoint
    Also can be filtered by id
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        queryset = Dish.objects.all()
        _id = self.request.query_params.get('id')

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class DishCreateAPIView(generics.CreateAPIView):
    """
    Creation method view to be used by POST API endpoint
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class DishUpdateAPIView(generics.UpdateAPIView):
    """
    Instance editing method view to be used by PUT/PATCH API endpoint
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class DishDeleteAPIView(generics.DestroyAPIView):
    """
    Deletion method view to be used by DELETE API endpoint
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]
