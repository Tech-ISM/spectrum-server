from django.contrib import admin

# Register your models here.
from referral.models import ReferCodeData, ReferData


class ReferCodeDataAdmin(admin.ModelAdmin):
    list_display = ["company_instance", "refer_code", "count_signup", "count_invoice", "count_redeemed",
                    "modified", "created"]


admin.site.register(ReferCodeData, ReferCodeDataAdmin)


class ReferDataAdmin(admin.ModelAdmin):
    list_display = ["refer_code_instance", "company_instance",
                    "modified", "created"]


admin.site.register(ReferData, ReferDataAdmin)
