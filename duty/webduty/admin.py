from django.contrib import admin
from django.db.models import fields
from django.utils.safestring import mark_safe
from .models import Duty, Office



@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['rank', "name",'number',]
admin.site.register(Duty)
admin.site.site_title = "DutyBooty"
admin.site.site_header = "DutyBooty" 