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
        'dishes',
    ]

    list_filter = [
        'restaurant',
    ]

    def dishes(self, obj):
        return " ,".join([str(i) for i in Dish.objects.filter(menu_id=obj.id)])


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu']



    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'menu':
            kwargs['required'] = False 
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
