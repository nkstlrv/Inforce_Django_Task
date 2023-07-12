from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'get_day', 'get_dishes', 'get_votes_count']

    def get_day(self, obj):
        return dict(Menu.WEEKDAY_CHOICES)[obj.day]

    def get_dishes(self, obj):
        return ", ".join([dish.name for dish in obj.dishes.all()])

    def get_votes_count(self, obj):
        return obj.vote_set.count()

    get_votes_count.short_description = 'Votes'
