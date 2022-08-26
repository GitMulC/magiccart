from django.contrib import admin
from .models import Subscriber

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')

    ordering = ('-date_subscribed',)

admin.site.register(Subscriber, SubscriberAdmin)
