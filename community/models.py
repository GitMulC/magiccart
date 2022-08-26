from django.db import models

# Create your models here.

class Community(models.Model):
    """ Commmunity model """
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField()
    url = models.URLField(max_length=1024)
    logo = models.ImageField()

    def __str__(self):
        return self.name
