from django.contrib import admin
from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'url',
    )


admin.site.register(Community, CommunityAdmin)
