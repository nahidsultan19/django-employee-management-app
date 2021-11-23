from django.contrib import admin
from . models import *

class EmployeeAdmin(admin.ModelAdmin):
	list_display=('name','email','position')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
