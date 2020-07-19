from django.contrib import admin
from .models import college,College_De,Company,Car,User,Community

# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['sid','name','city','age']

admin.site.register(college,CollegeAdmin)

class College_DeAdmin(admin.ModelAdmin):
    list_display = ['college','rn','brnch','addr','yr']

admin.site.register(College_De,College_DeAdmin)


class Company_DAdmin(admin.ModelAdmin):
    list_display = ['cid','cname']

admin.site.register(Company,Company_DAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ['mname','price','company']

admin.site.register(Car,CarAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['uid','uname']

admin.site.register(User,UserAdmin)

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['cname']

admin.site.register(Community,CommunityAdmin)
