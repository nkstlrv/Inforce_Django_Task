from django.db import models


class RestaurantCostChoices(models.IntegerChoices):
    """
    Choices for cost field in Restaurant model
    """
    LOW = 1, ('Low')
    MID = 2, ('Mid')
    HIGH = 3, ('High')
    
    
class DishDayChoices(models.IntegerChoices):
    """
    Choices for day of the week
    """
    EVERYDAY = 0, ('Everyday')
    MONDAY = 1, ('Monday')
    TUESDAY = 2, ('Tuesday')
    WEDNESDAY = 3, ('Wednesday')
    THURSDAY = 4, ('Thursday')
    FRIDAY = 5, ('Friday')
    SATURDAY = 6, ('Saturday')
    SUNDAY = 7, ('Sunday')