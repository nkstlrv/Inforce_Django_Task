from django.db import models
from .choises import RestaurantCostChoices


class Restaurant(models.Model):
    """
    Model to store main info about restaurants:
    - their name, address, cuisine, cost(low, mid, high)
    - menu (foreign key to Menu model)
    """
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    cuisine = models.CharField(max_length=300, null=True, default=None)
    cost = models.CharField(choices=RestaurantCostChoices.choices, default=RestaurantCostChoices.MID)
    
    
    def __str__(self):
        return f"{self.name} | {self.address}"
    


