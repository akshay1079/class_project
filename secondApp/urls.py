from django.urls import path
from . import views

urlpatterns = [
    path('v2/',views.view2),
    path('v1/',views.view1),
    path('cal/',views.calcview),
]