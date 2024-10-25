import uuid
from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
