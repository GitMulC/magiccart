from django.db import models
from cloudinary.models import CloudinaryField

class Card(models.Model):
    name = models.CharField(max_length=30)
    color = CloudinaryField('mana_symbol')
    oracle_text = models.CharField(max_length=254, blank=True)
    flavor_text = models.CharField(max_length=254, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    set = models.CharField(max_length=254)
    rarity = models.CharField(max_length=254)
    cmc = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    version = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name
