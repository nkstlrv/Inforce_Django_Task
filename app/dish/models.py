from django.db import models


class Dish(models.Model):
    """
    Model for specific dish to be related to menu model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
