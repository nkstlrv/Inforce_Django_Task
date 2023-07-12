from django.contrib import admin
from .models import Restaurant, Dish


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'phone_number',
        'cuisine',
        'cost',
        'delivery',
        'dishes',
    ]
    
    search_fields = [
        'name',
        'dish',
        'cuisine'
    ]
    
    list_filter = ['cost', 'delivery']
    
    def dishes(self, obj):
        return obj.dishs.all()
    
    
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'day',
        'price',
        'restaurants_to_eat',
    ]
    
    search_fields = [
        'name',
        'day',
    ]
    
    list_filter = ['day']

    def restaurants_to_eat(self, obj):
        return obj.restaurants.all()