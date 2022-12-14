from django.db import models


class Subscriber(models.Model):
    """ Mail list subscriber model """

    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
