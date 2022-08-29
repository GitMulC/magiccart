from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'location',)

    ordering = ('date',)


admin.site.register(Event, EventAdmin)
