from django.db import models
from django.contrib.auth.models import User
from autentifikasi.models import Profile  # Impor Profile
from addProduct.models import Food  # Impor Food
import uuid

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    liked_foods = models.ManyToManyField(Food, blank=True) 
    name = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.profile.user.username}'s bookmarks"