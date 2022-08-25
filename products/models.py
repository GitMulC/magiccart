from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Card(models.Model):
    name = models.CharField(max_length=30)
    mana_cost = models.CharField(max_length=254, blank=True)
    cmc = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    type_line = models.CharField(max_length=254)
    oracle_text = models.TextField(blank=True)
    flavor_text = models.TextField(blank=True)
    colors = models.JSONField()
    card_img = CloudinaryField('card', null=True, blank=True)
    card_img_url = models.URLField(max_length=1024, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    user_favorite = models.ManyToManyField(User, related_name='user_favorite', blank=True)

    def __str__(self):
        return self.name
