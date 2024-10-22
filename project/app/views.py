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
