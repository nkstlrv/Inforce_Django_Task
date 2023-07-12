from django.contrib import admin
from .models import Restaurant, Dish, Vote


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


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_menus']

    def get_menus(self, obj):
        return ", ".join([menu.restaurant.name for menu in obj.menu_set.all()])

    get_menus.short_description = 'Menus'
    
    
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['menu', 'employee']
