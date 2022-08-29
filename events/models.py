from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    date = models.DateTimeField()
    contact_info = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name
