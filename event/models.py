from __future__ import unicode_literals

from django.db import models


# Create your models here.
from register.models import UserData


class EventData(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    round_name = models.CharField(max_length=120, blank=True, null=True)
    rules = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='event/', default="/media/event/default.png")
    image_blur = models.ImageField(upload_to='event/', default="/media/event/default.png")
    image_landscape = models.ImageField(upload_to='event/', default="/media/event/default.png")
    time = models.CharField(max_length=120, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(default=1, blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    day = models.IntegerField(default=0, blank=True, null=True)
    attendees = models.IntegerField(default=0, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    prize_description = models.CharField(max_length=120, blank=True, null=True)
    round = models.IntegerField(default=1, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name


class UserEventData(models.Model):
    user = models.ForeignKey(UserData, null=True)
    event = models.ForeignKey(EventData, null=True)
    participated = models.IntegerField(default=0, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.user.name


class OrganiserData(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    mobile = models.CharField(max_length=120, blank=True, null=True)
    event = models.ForeignKey(EventData, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name
