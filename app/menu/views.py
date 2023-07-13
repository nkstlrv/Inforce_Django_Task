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
    List all Menus in DB

    Restaurant represents as ID

    Days of the week represents as integer
    0 - menu available every day
    1 - 7 --> Monday - Sunday

    To get all menus by providing specific day there is get_queryset() method
    """
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
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
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class MenuUpdateAPIView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class MenuDeleteAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class TodayBestMenusAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        today = date.today()

        top_menus = Menu.objects.filter(day=today.weekday()).annotate(
            vote_count=Count('vote')
        ).exclude(vote_count__lt=1).order_by('-vote_count')[:3]

        serializer = MenuSerializer(top_menus, many=True)
        return Response(serializer.data)
