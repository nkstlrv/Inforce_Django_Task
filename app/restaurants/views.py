from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated


class RestaurantListAPIView(generics.ListAPIView):
    """
    List all Restaurants in DB
    """
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

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
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None),
                        phone_number=self.request.data.get('phone_number', None))


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
