from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,Order
from .forms import StudentForm,CustomerForm,OrderForm
from django import forms
# Create your views here.
#HTML form
def addCustomer(request):
    if request.method == "POST":
        n = request.POST['cname']
        a = request.POST[ 'addr']
        e = request.POST[ 'email']
        m = request.POST['mono']
        c = Customer(cname=n,caddr=a,cemail=e,cphone=m)
        c.save()
        #template_name = 'EcommerceApp/all_cust.html'
        #context = {'msg':'Hey New Customer Added Successfully....'}
        #return render(request,template_name,context)
        #return HttpResponse('Added successfully')
        return redirect('/ecom/ord')

    elif request.method == "GET":
        return render(request,'EcommerceApp/addCust.html')


def allCustomers(request):
    cust = Customer.objects.all()
    template_name = 'EcommerceApp/all_cust.html'
    context = {'customers':cust}
    return render(request,template_name,context)

#model Form
def addorder(request):
    if request.method == 'POST':
        print('POST req. received...')
        form = OrderForm(request.POST)
        if form.is_valid():
            print('DATA is valid....')
            form.save()
        return redirect('/ecom/vc')
    else:
        print('Get req. received....')
        ord = OrderForm()
        template_name = 'EcommerceApp/ord.html'
        context = {'form': ord}
        return render(request, template_name, context)




def allOrder(request):
    ord = Order.objects.all()
    template_name = 'EcommerceApp/all_orders.html'
    context = {'order':ord}
    return render(request,template_name,context)

#Django Form
def addCustomerDF(request):
    if request.method == 'POST':
        print('POST req. rec for addCustomers')
        form = CustomerForm(request.POST)  #object of Form With Data
        if form.is_valid():
            print('Data is Valid... ')
            n = form.cleaned_data['cname']
            a = form.cleaned_data['caddr']
            e = form.cleaned_data['cemail']
            p = form.cleaned_data['cphone']
            print(n,a,e,p)
            custObj = Customer(cname=n,caddr=a,cemail=e,cphone=p)
            custObj.save()
        return redirect('/ecom/ord')
        #return HttpResponse('POST Req. Recvd')

    else:
        print("GET req.recd from addcustomer..")
        cust = CustomerForm()           #Blank Form Object
        template_name = 'EcommerceApp/adc.html'
        context = {'form': cust}
        return render(request, template_name, context)


#django class Form
def addStudent(request):
    template_name = 'EcommerceApp/addStu.html'
    stu = StudentForm()
    context = {'form':stu}
    return render(request,template_name,context)

