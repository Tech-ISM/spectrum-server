from django.contrib import admin

# Register your models here.
from customs.models import KeysData


class KeysDataAdmin(admin.ModelAdmin):
    list_display = ["key", "value", "created", "modified"]


admin.site.register(KeysData, KeysDataAdmin)
