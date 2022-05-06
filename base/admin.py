from django.contrib import admin

from base.models import Task, Employee, EmployeesImport

# Register your models here.
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(EmployeesImport)

