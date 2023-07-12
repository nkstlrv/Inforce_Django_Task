from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint
    path('list/', views.DishListAPIView.as_view(), name='dish_list'),

    # POST endpoint
    path('create/', views.DishCreateAPIView.as_view(), name='dish_create'),

    # PUT endpoint
    path('update/<int:pk>/', views.DishUpdateAPIView.as_view(), name='dish_update'),

    # DELETE endpoint
    path('delete/<int:pk>/', views.DishDeleteAPIView.as_view(), name='dish_delete'),

]
