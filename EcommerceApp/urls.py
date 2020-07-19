from django.urls import path
from . import views

urlpatterns = [
    path('ac/',views.addCustomer,name='addCustomer'),
    path('vc',views.allCustomers,name='allCustomers'),
    path('ord',views.addorder,name='addorder'),
    path('vo',views.allOrder,name='allOrder'),
    path('ads',views.addStudent,name='addStudent'),
    path('adc',views.addCustomerDF,name='addCust'),

]