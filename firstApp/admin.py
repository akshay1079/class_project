from django.contrib import admin
from .models import Employee
from .models import Student,StuD

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','name','email','salary']

admin.site.register(Employee,EmployeeAdmin)

#Student class

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','name','email','marks']

admin.site.register(Student,StudentAdmin)


class StuDAdmin(admin.ModelAdmin):
    list_display = ['city','rn','yr','student']