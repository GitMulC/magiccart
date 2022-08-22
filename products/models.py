from django.db import models
from cloudinary.models import CloudinaryField

class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Card(models.Model):
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    color = CloudinaryField('mana_symbol')
    oracle_text = models.TextField(blank=True)
    flavor_text = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    set = models.TextField(blank=True)
    rarity = models.TextField(blank=True)
    cmc = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    card_img = CloudinaryField('card', null=True, blank=True)
    card_img_url = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return self.name
