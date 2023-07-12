from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint
    path('list/', views.VoteListAPIView.as_view(), name='vote_list'),

    # POST endpoint
    path('create/', views.VoteCreateAPIView.as_view(), name='vote_create'),

    # DELETE endpoint
    path('delete/<int:pk>/', views.VoteDeleteAPIView.as_view(), name='vote_delete'),

    # PUT endpoint
    path('update/<int:pk>/', views.VoteUpdateAPIView.as_view(), name='vote_update'),

]
