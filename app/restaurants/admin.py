from django.contrib import admin
from .models import Restaurant, Dish, Menu, Vote


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


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'get_day', 'get_dishes', 'votes']

    def get_day(self, obj):
        return dict(Menu.WEEKDAY_CHOICES)[obj.day]

    def get_dishes(self, obj):
        return ", ".join([dish.name for dish in obj.dishes.all()])


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_menus']

    def get_menus(self, obj):
        return ", ".join([menu.restaurant.name for menu in obj.menu_set.all()])

    get_menus.short_description = 'Menus'
    
    
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['menu', 'employee']
