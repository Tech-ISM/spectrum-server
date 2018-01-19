from __future__ import unicode_literals

from django.db import models


class NotificationData(models.Model):
    notification_title = models.CharField(max_length=150, blank=False, null=False)
    notification_message = models.CharField(max_length=600, blank=False, null=False)
    notification_time = models.CharField(max_length=600, blank=False, null=False)
    notification_date = models.CharField(max_length=600, blank=False, null=False)
    notification_image = models.ImageField(upload_to='notification_image/', blank=True)
    notification_event_id = models.IntegerField(default=1, blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return str(self.notification_title)
