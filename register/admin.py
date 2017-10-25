from django.contrib import admin

# Register your models here.
from register.models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile", "created", "modified"]


admin.site.register(UserData, UserDataAdmin)
