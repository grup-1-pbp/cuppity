from django.db import models
import uuid
class Food(models.Model):
    PREFERENCE_CHOICES = [
        ('Indo', 'Indonesia'),
        ('Chin', 'Chinese'),
        ('West', 'Western'),
        ('Japan', 'Japanese'),
        ('India,', 'Indian')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    restaurant = models.CharField(max_length=255)
    deskripsi = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.CharField(max_length=255)

    preference = models.CharField(
        max_length=255,
        choices=PREFERENCE_CHOICES
    )
    image_url = models.URLField(max_length=500, blank=True, null=True)