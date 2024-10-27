from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    budget = models.IntegerField(blank=True, null=True, default=0)
    profile_image = models.URLField(max_length=500, blank=True, null=True, default="https://tse3.mm.bing.net/th?id=OIP.lLmJV7N4bgAwEBtziWijSQHaJL&pid=Api&P=0&h=180")

    def __str__(self):
        return f'{self.user.username} - {self.role} '
