from django.contrib import admin
from .models import UserSettings, Profile


class SettingUserSettings(admin.ModelAdmin):
    list_display = ('user', 'status')

admin.site.register(UserSettings,SettingUserSettings)
admin.site.register(Profile)

