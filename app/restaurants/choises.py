from django.db import models


class RestaurantCostChoices(models.IntegerChoices):
    """
    Choices for cost field in Restaurant model
    """
    LOW = 1, ('Low')
    MID = 2, ('Mid')
    HIGH = 2, ('High')