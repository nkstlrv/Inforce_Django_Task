from django.contrib import admin
from .models import Restaurant, Vote


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'delivery',
        'phone_number',
    ]

    list_filter = [
        'delivery',
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['menu', 'employee']
