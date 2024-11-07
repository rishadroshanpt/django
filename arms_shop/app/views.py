from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import *
from django.contrib import messages


# Create your views here.

def arms_login(req):
    if 'arms' in req.session:
        return redirect(home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['arms']=uname   #create session
            return redirect(home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(arms_login)
    else:
        return render(req,'login.html')
    
def home(req):
    if 'arms' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'data':data})
    else:
        return redirect(arms_login)
    
def arms_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(arms_login)

def add_prod(req):
    if 'arms' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            img=req.FILES['img']
            rtng=req.POST['rtng']
            data=Product.objects.create(pro_id=prd_id,name=prd_name,price=prd_price,offer_price=ofr_price,img=img,rating=rtng)
            data.save()
            return redirect(add_prod)
        else:
            return render(req,'shop/add_prod.html')
    else:
        return redirect(arms_login)
    
def edit(req,pid):
    if 'arms' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            rtng=req.POST['rtng']
            img=req.FILES.get('img')
            if img:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,offer_price=ofr_price,rating=rtng)
                data=Product.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,offer_price=ofr_price,rating=rtng)
            return redirect(home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit.html',{'product':data})
    else:
        return redirect(arms_login)

def delete(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    return redirect(home)