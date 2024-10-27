from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    budget = models.IntegerField(blank=True, null=True)
    profile_image = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user
    
    def clean_role(self):
        role = self.cleaned_data['role']
        return role
    
    def clean_budget(self):
        budget = self.cleaned_data['budget']
        return budget
    

    def clean_image_url(self):
        profile_image = self.cleaned_data['profile_image']
        return profile_image