from django.db import models


class Restaurant(models.Model):
    """
    Model of the Restaurant instances
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
