from django.contrib import admin
from .models import Restaurant, Dish, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'address',
        'delivery',
        'phone_number',
        # 'menu',
    ]
    
    list_filter = [
        'delivery',
    ]
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    
    list_display = [
        'restaurant',
        'get_day_display',
    ]

    list_filter = [
        'restaurant',
    ]
    


@admin.register(Dish)   
class DishAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'get_menu',
    ]


    def get_menu(self, obj):
        return obj.menu