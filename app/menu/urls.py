from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint for list of menus. If query parameters are provided, request is being filtered
    path('menu/list/', views.MenuListAPIView.as_view(), name='menu_list'),

    # POST endpoint to create new menu
    path('menu/create/', views.MenuCreateAPIView.as_view(), name='menu_create'),

    # PUT/PUSH endpoint to update menu
    path('menu/update/<int:pk>/', views.MenuUpdateAPIView.as_view(), name='menu_update'),

    # DELETE endpoint for menu
    path('menu/delete/<int:pk>/', views.MenuDeleteAPIView.as_view(), name='menu_delete'),
    
    # GET endpoint to show best today's menus according to votes
    path('menu/today-best/', views.TodayBestMenusAPIView.as_view(), name='best_menus'),


]
