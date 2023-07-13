from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class RestaurantListAPIView(generics.ListAPIView):
    """
    Returns all Restaurants
    Also can be filtered by query parameters:
    - id,
    - delivery option
    """
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        _id = self.request.query_params.get('id')
        delivery = self.request.query_params.get('delivery')

        if _id:
            queryset = queryset.filter(id=_id)

        if delivery:
            queryset = queryset.filter(delivery=delivery)

        return queryset


class RestaurantCreateAPIView(generics.CreateAPIView):
    """
    Creation method view to be used by POST API endpoint
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None),
                        phone_number=self.request.data.get('phone_number', None))


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    """
    Instance editing method view to be used by PUT/PATCH API endpoint
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    """
    Deletion method view to be used by DELETE API endpoint
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]
