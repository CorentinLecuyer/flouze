from django.contrib import admin
from .models import Analysis, RootCause, Deductions, Action, Owner, CollectorsInput


class SettingDeductions(admin.ModelAdmin):
    list_display = ('assignment', 'payer', 'status', 'type', 'clerks')


class SettingRootcause(admin.ModelAdmin):
    list_display = ('name', 'analysis')


class SettingAction(admin.ModelAdmin):
    list_display = ('name', 'analysis', 'rootcause')


class SettingCollectorsInput(admin.ModelAdmin):
    list_display = ('id', 'unikey', 'analysis', 'rootcause', 'action', 'owner', 'nb_com')


admin.site.register(Deductions, SettingDeductions)
admin.site.register(Analysis)
admin.site.register(RootCause, SettingRootcause)
admin.site.register(Action, SettingAction)
admin.site.register(Owner)
admin.site.register(CollectorsInput, SettingCollectorsInput)
