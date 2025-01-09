from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    data=Courses.objects.all()
    return render(req,'index.html',{'data':data})
def course(req,id):
    if req.method=='POST':
        Name=req.POST['Name']
        Mobile=req.POST['Mobile']
        Email=req.POST['Email']
        Msg=req.POST['Msg']
        data=enquiry.objects.create(name=Name,mobile=Mobile,email=Email,msg=Msg)
        data.save()
    data=Courses.objects.get(pk=id)
    return render(req,'course.html',{'data':data})
    
