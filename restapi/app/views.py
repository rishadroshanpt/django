from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.

def usr_def_serializers(req):
    if req.method=='GET':
        data=student.objects.all()
        d=usr_serializers(data,many=True)
        return JsonResponse(d.data,safe=False)