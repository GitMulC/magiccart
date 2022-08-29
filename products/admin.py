from django.contrib import admin
from .models import Card, Type


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colors',
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
