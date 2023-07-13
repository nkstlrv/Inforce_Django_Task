from django.contrib import admin
from .models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """
    Needed for better UI model representation on admin panel
    """
    list_display = ['menu', 'employee']
