from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.
def view1(request):
    return HttpResponse("Hello from AppName-view-1")

def login(request):
    return render(request,'firstApp/login.html')

def view3(request):
    template_name="firstApp/try.html"
    return render(request,template_name)


def ty(request):
    return render(request,"firstApp/gallary.html")

def addStudent(request):
    template_name = 'firstApp/addstu.html'
    stu = StudentForm()
    context = {'form':stu}
    return render(request,template_name,context)
