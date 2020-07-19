from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Employee

# Create your views here.
def view1(request):
    return HttpResponse("view from -----1")

def add(request):
    num1 =int(input("Enter First Num:-"))
    num2 = int(input("Enter Second Num:-"))
    tot = num1 + num2
    context = {'tot':tot}
    template_name = 'third/a.html'
    return render(request,template_name,context)

def home(request):
    template_name='third/home.html'
    context={}
    return render(request,template_name,context)

def about(request):
    template_name='third/about.html'
    context={}
    return render(request,template_name,context)

def contact(request):
    template_name='third/contact.html'
    context={}
    return render(request,template_name,context)


def allStudent(request):
    #select * from <table_name>    #mysql Query
    #objs = Model.objects.all()    #django ORM
    students = Student.objects.all()
    template_name = 'third/allStudent.html'
    context = {'stu':students}
    return render(request,template_name,context)



def allEmployee(request):
    #select * from <table_name>    #mysql Query
    #objs = Model.objects.all()    #django ORM
    employees = Employee.objects.all()
    template_name = 'third/allEmployee.html'
    context = {'emp':employees}
    return render(request,template_name,context)