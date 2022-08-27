# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
# from products.models import Card

# # Create your models here.
# class Wishlist(models.Model):
#     card = models.ForeignKey('products.Card', on_delete=models.SET_NULL)
#     date_added = models.DateField(auto_now=True)
#     price = models.ForeignKey('products.Card', on_delete=models.SET_NULL)
#     user = models.ForeignKey('profiles.User', on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.card
