from django.contrib import admin

# Register your models here.
from notification.models import NotificationData


class NotificationDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'notification_title', 'notification_message', 'notification_image', 'created']


admin.site.register(NotificationData, NotificationDataAdmin)
