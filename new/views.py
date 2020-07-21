from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def newStu(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data['rn']
            n = form.cleaned_data['name']
            m = form.cleaned_data['marks']
            p2 = form.cleaned_data['pass2']
            s = Student(rn=r,name=n,marks=m,pw=p2)
            s.save()
            print('Student Added...')
            return redirect(allStudent)
    else:
        form = StudentForm()

    template_name = "new/new.html"
    context = {'form':form}
    return render(request,template_name,context)


def allStudent(request):
    stu_objs = Student.objects.all()
    template_name = 'new/allStu.html'
    context = {'allStu':stu_objs}
    return render(request,template_name,context)