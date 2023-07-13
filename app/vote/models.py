from datetime import date
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from menu.models import Menu


class Vote(models.Model):
    """
    Model for employees votes
    Each employee can vote only for one menu at a time
    It is option only to vote for todays menus
    """
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.username} | {self.menu}"

    # Save and Update methods are overridden so today's only menu validation works
    def save(self, *args, **kwargs):
        today = date.today()
        if self.menu.day != today.weekday():
            raise ValidationError("Voting is only allowed for today's Menu")

        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        today = date.today()
        if self.menu.day != today.weekday():
            raise ValidationError("Voting is only allowed for today's Menu")

        super().update(*args, **kwargs)
