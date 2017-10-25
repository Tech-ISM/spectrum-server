from __future__ import unicode_literals

from django.db import models


# Create your models here.
class EventData(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='event/', default="/media/event/default.png")
    time = models.CharField(max_length=120, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    day = models.IntegerField(default=0, blank=True, null=True)
    attendees = models.IntegerField(default=0, blank=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name
