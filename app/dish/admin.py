from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_menus']

    def get_menus(self, obj):
        return ", ".join([menu.restaurant.name for menu in obj.menu_set.all()])

    get_menus.short_description = 'Menus'
