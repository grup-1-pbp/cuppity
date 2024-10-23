from django.db import models
from django.contrib.auth.models import User  # Assuming you have user authentication
from addProduct.models import Food


class Review(models.Model):
    food = models.ForeignKey('addProduct.Food', on_delete=models.CASCADE, related_name='food_reviews')  # Link to Food
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User who gave the review
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.food.name}'

    class Meta:
        ordering = ['-created_at']  # Most recent reviews first
