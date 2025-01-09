from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def userForm(req):
    if req.method=='POST':
        form1=user_form(req.POST)
        if form1.is_valid():
            roll=form1.cleaned_data['roll_no']
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            data=Student.objects.create(roll_no=roll,name=name,age=age,email=email)
            data.save()
            return redirect(userForm)
    form=user_form()
    return render(req,'user_form.html',{'form':form})

def modelForm(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
        return redirect(modelForm)
    else:
        form=model_form()
        return render(req,'model_form.html',{'form':form})