from django.contrib import admin

from api.models import DeviceToken


# Register your models here.
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']


admin.site.register(DeviceToken, DeviceTokenAdmin)
