from django.db import models


class Restaurant(models.Model):
    """
    Model of the restaurant
    Fields:
    - name of the restaurant
    - address of the restaurant
    - is there a delivery option
    -phone number for booking or delivery

    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, default=None)
    delivery = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, default=None)

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
        (0, 'Everyday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )

    name = models.CharField(max_length=50, default='Unknown Menu')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, default=None)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY_CHOICES, default=0)

    def get_day_display(self):
        """
        Method returns word-representation of weekdays instead of choices numbers
        """
        return dict(Menu.WEEKDAY_CHOICES)[self.day]

    def __str__(self):
        return f"Menu of {self.restaurant.name}"


class Dish(models.Model):
    """
    Model for specific dish to be related to menu model
    """
    name = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name
