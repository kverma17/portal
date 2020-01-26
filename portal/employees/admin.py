from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name', 'pan', 'age', 'gender', 'email', 'city']

admin.site.register(Employee, EmployeeAdmin)