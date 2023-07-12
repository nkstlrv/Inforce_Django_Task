from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint | query parameters filter available
    path('list/', views.MenuListAPIView.as_view(), name='menu_list'),

    # POST endpoint 
    path('create/', views.MenuCreateAPIView.as_view(), name='menu_create'),

    # PUT/PUSH endpoint 
    path('update/<int:pk>/', views.MenuUpdateAPIView.as_view(), name='menu_update'),

    # DELETE endpoint 
    path('delete/<int:pk>/', views.MenuDeleteAPIView.as_view(), name='menu_delete'),
    
    # GET endpoint 
    path('today-best/', views.TodayBestMenusAPIView.as_view(), name='best_menus'),


]
