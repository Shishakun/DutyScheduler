from django.contrib import admin
from django.db.models import fields
from django.utils.safestring import mark_safe
from .models import Duty, Fakultet, Office, Rank



@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['get_rank',"surname", "name",'get_number',]

    def get_rank(self,obj):
        return "\n".join([p.rank for p in obj.rank.all()])

    def get_number(self,obj):
        return "\n".join([p.number for p in obj.number.all()])


admin.site.register(Rank)
admin.site.register(Fakultet)
admin.site.register(Duty)


admin.site.site_title = "DutyBooty"
admin.site.site_header = "DutyBooty" 