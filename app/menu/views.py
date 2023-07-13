from datetime import date, timedelta
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class MenuListAPIView(generics.ListAPIView):
    """
    Returns all Menus
    Also can be filtered by query parameters:
    - id,
    - day (number, today/tomorrow)
    - restaurant ID and ID of the Menu
    """
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        queryset = Menu.objects.all()
        day = self.request.query_params.get('day')
        restaurant_id = self.request.query_params.get('restaurant_id')
        _id = self.request.query_params.get('id')

        if day:
            try:
                day = int(day)
            except ValueError:
                if day.lower() == 'today':
                    today = date.today()
                    day = today.weekday()
                elif day.lower() == 'tomorrow':
                    tomorrow = date.today() + timedelta(days=1)
                    day = tomorrow.weekday()
                else:
                    day = None

            if day is not None:
                queryset = queryset.filter(day=day)

        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)

        if _id:
            queryset = queryset.filter(id=_id)

        return queryset


class MenuCreateAPIView(generics.CreateAPIView):
    """
    Creation method view to be used by POST API endpoint
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class MenuUpdateAPIView(generics.UpdateAPIView):
    """
    Instance editing method view to be used by PUT/PATCH API endpoint
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class MenuDeleteAPIView(generics.DestroyAPIView):
    """
    Deletion method view to be used by DELETE API endpoint
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class TodayBestMenusAPIView(APIView):
    """
    Returns best Menu (Menus) for today according to employees votes
    """
    permission_classes = [IsAuthenticated]

    # Remove attribute to run pytest
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        today = date.today()

        top_menus = Menu.objects.filter(day=today.weekday()).annotate(
            vote_count=Count('vote')
        ).exclude(vote_count__lt=1).order_by('-vote_count')[:3]

        serializer = MenuSerializer(top_menus, many=True)
        return Response(serializer.data)
