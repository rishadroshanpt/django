from django.shortcuts import render
from django.http import HttpResponse
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