from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
def fun1(req):
    return HttpResponse('Hello World!')
def fun2(req):
    return HttpResponse('hoooo')
def fun3(req,a):
    return HttpResponse(a)
def task1(req,salary,year):
    if year>5:
        bonus=(salary/100)*5
        return HttpResponse(bonus)
    else:
        return HttpResponse('Year of service is less than 5')
def task2(req,city):
    if city=='Delhi':
        return HttpResponse('Red Fort')
    elif city=='Agra':
        return HttpResponse('Taj Mahal')
    elif city=='Jaipur':
        return HttpResponse('Jal Mahal')
    else:
        return HttpResponse('Invalid input !')
def task3(req,num):
    n=num%10
    if n%3==0:
        return HttpResponse('The last digit of the number is divisible by 3.')
    else:
        return HttpResponse('The last digit of the number is not divisible by 3.')
def task4(req,ch):
    if ch==1:
        return HttpResponse('Sunday')
    elif ch==2:
        return HttpResponse('Monday')
    elif ch==3:
        return HttpResponse('Tuesday')
    elif ch==4:
        return HttpResponse('Wednesday')
    elif ch==5:
        return HttpResponse('Thursday')
    elif ch==6:
        return HttpResponse('Friday')
    elif ch==7:
        return HttpResponse('Saturday')
    else:
        return HttpResponse('Invalid choice !')
def task5(req,price):
    if price>100000:
        tax=price/100*15
    elif price>50000 and price<=100000:
        tax=price/100*10
    else:
        tax=price/100*5
    return HttpResponse(tax)
def task6(req,units):
    if units<=100:
        return HttpResponse('No charge')
    elif units>100 and units<=200:
        charge=(units-100)*5
        return HttpResponse(charge)
    else:
        charge=(units-200)*10
        return HttpResponse(charge+500)
def demo(req):
    a='boiiii'
    return render(req,'demo.html',{'data':a})
users=[{'id':'1','name':'anu','age':'12','email':'anu@gmail.com'}]
def display(req):
    return render(req,'user_reg.html',{'users':users})
def add(req):
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        users.append({'id':id,'name':name,'age':age,'email':email})
        return redirect(display)
    else:
        return redirect(display)
def edit_user(req,id):
    user=''
    for i in users:
        if i['id']==id:
            user=i
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        user['id']=id
        user['name']=name
        user['age']=age
        user['email']=email
        return redirect(display)
    return render(req,'edit_user.html',{'user':user})
def delete_user(req,id):
    for i in users:
        if i['id']==id:
            users.remove(i)
    return redirect(display)
def index(req):
    return render(req,'index.html')
def disStd(req):
    data=Student.objects.all()
    return render(req,'disStd.html',{'std':data})
def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        data=Student.objects.create(roll_no=roll,name=name,age=age,email=email)
        data.save()
        return redirect(disStd)
    else:
        return render(req,'add_std.html')
def edt_std(req,id):
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,email=email)
        return redirect(disStd)
    return render(req,'edit_std.html',{'data':data})

def dlt_std(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(disStd)