from django.db import models
import uuid
class Food(models.Model):
    PREFERENCE_CHOICES = [
        ('Indo', 'Indonesia'),
        ('Chin', 'Chinese'),
        ('West', 'Western'),
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

    def __str__(self):
        return self.name
    
    def clean_name(self):
        name = self.cleaned_data['name']
        return name
    
    def clean_price(self):
        price = self.cleaned_data['price']
        return price
    
    def clean_deskripsi(self):
        deskripsi = self.cleaned_data['deskripsi']
        return deskripsi
    def clean_restaurant(self):
        restaurant = self.cleaned_data['restaurant']
        return restaurant
    def clean_preference(self):
        preference = self.cleaned_data['preference']
        return preference
    def clean_image_url(self):
        image_url = self.cleaned_data['image_url']
        return image_url
    
