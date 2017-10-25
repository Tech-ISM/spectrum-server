from django.contrib import admin

# Register your models here.
from event.models import EventData


class EventDataAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "modified"]


admin.site.register(EventData, EventDataAdmin)
