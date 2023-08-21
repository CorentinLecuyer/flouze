from django.contrib import admin
from .models import Customer, PayerGroup


class SettingCustomer(admin.ModelAdmin):
    list_display = ('payer_name', 'payer', 'channel')


class SettingPayerGroup(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Customer,SettingCustomer)
admin.site.register(PayerGroup,SettingPayerGroup)