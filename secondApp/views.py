from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse("view from ---1")


def view2(request):
    #return HttpResponse("view from ---2")
    context = {'name':'cjc','rn':19,'marks':19.34,'li':[1,2,3,4,5,6],'age':30}
    template_name = 'secondApp/home.html'
    return render(request,template_name,context)

def calcview(request):
    print(request.POST)
    n1 = int(request.POST.get('num1',0))
    n2 = int(request.POST.get('num2',0))
    tot = n1 + n2
    template_name = 'secondApp/cal.html'
    context = {'total':tot}
    return render(request,template_name,context)