from django.urls import path
from . import views

urlpatterns = [

    # GET endpoint
    path('vote/list/', views.VoteListAPIView.as_view(), name='vote_list'),

    # POST endpoint
    path('vote/create/', views.VoteCreateAPIView.as_view(), name='vote_create'),

    # DELETE endpoint
    path('vote/delete/<int:pk>/', views.VoteDeleteAPIView.as_view(), name='vote_delete'),

    # PUT endpoint
    path('vote/update/<int:pk>/', views.VoteUpdateAPIView.as_view(), name='vote_update'),

]
