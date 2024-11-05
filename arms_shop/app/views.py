from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import os
from django.contrib import messages


# Create your views here.

def login(req):
    if 'arms' in req.session:
        return redirect(shp_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['arms']=uname   #create session
            return redirect(shp_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(login)
    
    else:
        return render(req,'login.html')
