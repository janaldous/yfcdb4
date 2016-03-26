from django.contrib import admin

from .models import Event, Attend


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'type', 'venue')

admin.site.register(Attend)