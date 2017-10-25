from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    mobile = models.CharField(max_length=120, primary_key=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    fcm = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.mobile