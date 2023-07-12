from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint for list of all dishes
    path('list/', views.DishListAPIView.as_view(), name='dish_list'),

    # POST endpoint to create new dish
    path('create/', views.DishCreateAPIView.as_view(), name='dish_create'),

    # PUT endpoint to update dish
    path('update/<int:pk>/', views.DishUpdateAPIView.as_view(), name='dish_update'),

    # DELETE endpoint for dish
    path('delete/<int:pk>/', views.DishDeleteAPIView.as_view(), name='dish_delete'),


]
