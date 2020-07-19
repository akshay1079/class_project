from django.urls import path
from .  import views

urlpatterns = [
    path('v1/',views.view1),
    path('lg',views.login),
    path('v3/',views.view3),
    path('ty',views.ty),
    path('ads',views.addStudent,name='AddStudent')
    ]