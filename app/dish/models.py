from django.db import models


class Dish(models.Model):
    """
    Distinct Dish entity to be related to menus
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
