from django.db import models
from .choices import RestaurantCostChoices, DishDayChoices
from django.core.validators import MinValueValidator


class Dish(models.Model):
    """
    Model to store available dishes and their day of availability
    - day (week day when this dish is available)
    - name (name of the dish)
    - price (price of the dish)
    """
    name = models.CharField(max_length=150)
    
    day = models.PositiveIntegerField(choices=DishDayChoices.choices, 
                                      default=DishDayChoices.EVERYDAY, 
                                      max_length=1)
    
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=True,
                                default=None,
                                validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} | {self.day}"


class Restaurant(models.Model):
    """
    Model to store main info about restaurants:
    - their name, address, cuisine, cost(low, mid, high)
    - phone number 
    - delivery option
    - menu (foreign key to Menu model)
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    cuisine = models.CharField(max_length=100, null=True, default=None)
    cost = models.PositiveSmallIntegerField(choices=RestaurantCostChoices.choices, 
                            default=RestaurantCostChoices.MID,
                            max_length=1)
    delivery = models.BooleanField(default=False)
    dish = models.ManyToManyField(Dish)

    def __str__(self):
        return f"{self.name} | {self.address}"
