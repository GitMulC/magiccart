from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from products.models import Card


class Wishlist(models.Model):
    card = models.ForeignKey('products.Card', on_delete=models.SET_NULL, null=True)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wishlist_user"
    )

    def __str__(self):
        return self.card
