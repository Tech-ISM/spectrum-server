from django.contrib import admin

# Register your models here.
from event.models import EventData, UserEventData


class EventDataAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created", "modified"]


admin.site.register(EventData, EventDataAdmin)


class UserEventDataAdmin(admin.ModelAdmin):
    list_display = ["user", "event", "created", "modified"]


admin.site.register(UserEventData, UserEventDataAdmin)


class OrganiserDataAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile", "created", "modified"]


admin.site.register(UserEventData, UserEventDataAdmin)
