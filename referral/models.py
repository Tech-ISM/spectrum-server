from __future__ import unicode_literals

from django.db import models

# Create your models here.
from register.models import UserData


class ReferCodeData(models.Model):
    company_instance = models.ForeignKey(UserData, blank=False)
    refer_code = models.CharField(max_length=255, default="")
    count_signup = models.PositiveIntegerField(default=0)
    count_invoice = models.PositiveIntegerField(default=0)
    count_redeemed = models.PositiveIntegerField(default=0)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.company_instance.mobile


class ReferData(models.Model):
    refer_code_instance = models.ForeignKey(ReferCodeData, blank=False)
    company_instance = models.ForeignKey(UserData, blank=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.company_instance.mobile

