from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    data=Course.objects.all()
    return render(req,'index.html',{'data':data})
def course(req,id):
    data=Course.objects.get(pk=id)
    return render(req,'course.html',{'data':data})
