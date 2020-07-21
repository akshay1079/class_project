from django.urls import path
from . import views

urlpatterns = [
    path('n',views.newStu,name='NewStudent'),
    path('a',views.allStudent,name='allStudent')
]