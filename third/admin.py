from django.contrib import admin
from .models import Student,Employee,Student_Details,Company,Cars,User,Community

# Register your models here.
#admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn','name','mark']

admin.site.register(Student,StudentAdmin)

#Employee----
#admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','name','email','salary']

admin.site.register(Employee,EmployeeAdmin)


class Student_DetailsAdmin(admin.ModelAdmin):
    list_display = ['city','pincode','email','student']

admin.site.register(Student_Details,Student_DetailsAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['cid','cname']

admin.site.register(Company,CompanyAdmin)

class CarsAdmin(admin.ModelAdmin):
    list_display = ['mname','price','company']

admin.site.register(Cars,CarsAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ['uid','uname']

admin.site.register(User,UserAdmin)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ['cname']

admin.site.register(Community,CommunityAdmin)