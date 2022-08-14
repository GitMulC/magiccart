from django.contrib import admin
from .models import Card, Type

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'type',
        'rarity',
        'price',
    )

    ordering = ('name',)

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Card, CardAdmin)
admin.site.register(Type, TypeAdmin)
