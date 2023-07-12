from datetime import date
from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Restaurant(models.Model):
    """
    Model of the restaurant
    Fields:
    - name of the restaurant
    - address of the restaurant
    - is there a delivery option
    -phone number for booking or delivery

    """
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, default=None)
    delivery = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, default=None)

    def __str__(self):
        return self.name


class Dish(models.Model):
    """
    Model for specific dish to be related to menu model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """
    Model of the menu
    Fields:
    - restaurant ID where this menu can be found
    - day when this menu is available
    """
    WEEKDAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY_CHOICES, default=0)
    dishes = models.ManyToManyField(Dish, blank=True)

    def __str__(self):
        return f"Menu of {self.restaurant.name} | {self.day}"


class Vote(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.username} | {self.menu}"

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
