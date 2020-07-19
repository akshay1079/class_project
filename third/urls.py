from django.urls import path
from . import views

urlpatterns = [
    path('v1/',views.view1),
    path('add/',views.add),
    path('hm/',views.home,name='home' ),
    path('ab/',views.about,name='about'),
    path('co/',views.contact,name='contact'),
    path('as/',views.allStudent),
    path('em/',views.allEmployee),

]