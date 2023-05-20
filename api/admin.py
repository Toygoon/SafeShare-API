from django.contrib import admin

from api.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_pw', 'name', 'mileage', 'mobile', 'registered_at', 'app_token']


admin.site.register(User, UserAdmin)
