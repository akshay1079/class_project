from django.contrib import admin
from .models import Customer,Order
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cname','caddr','cemail','cphone']

admin.site.register(Customer,CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pname','pbatch_no','pqty','pprice','pseller','customer']

admin.site.register(Order,OrderAdmin)