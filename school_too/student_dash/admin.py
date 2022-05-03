from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_dash.models import ChurchLeader, Stats, Church, Report, FinancialReport

class ChurchLeaderAdmin(UserAdmin):
    list_display = ('email','username','church_name','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username','church_name')
    readonly_fields=('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ChurchLeader,ChurchLeaderAdmin)
admin.site.register(Stats)
admin.site.register(Church)
admin.site.register(Report)
admin.site.register(FinancialReport)