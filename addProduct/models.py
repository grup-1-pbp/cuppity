from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preference = models.CharField(
        max_length=255,
        choices=[('Veg', 'Vegetarian'), ('Non-Veg', 'Non-Vegetarian')]
    )
    image_url = models.URLField(max_length=500, blank=True, null=True) 

    def __str__(self):
        return self.name
