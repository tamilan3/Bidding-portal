# models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AntiqueProduct(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='antique_products/', blank=True, null=True)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    bidding_closed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Bidding(models.Model):
    product = models.ForeignKey(AntiqueProduct, related_name='biddings', on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bidding_price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid for {self.product.title} by {self.bidder.username}"
    
    