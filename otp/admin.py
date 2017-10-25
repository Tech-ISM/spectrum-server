from django.contrib import admin

# Register your models here.
from otp.models import OtpData


class OtpDataAdmin(admin.ModelAdmin):
    list_display = ["mobile", "otp", "flag", "created", "modified"]


admin.site.register(OtpData, OtpDataAdmin)
