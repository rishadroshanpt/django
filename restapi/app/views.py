from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def usr_def_serializers(req):
    if req.method=='GET':
        data=student.objects.all()
        d=usr_serializers(data,many=True)
        return JsonResponse(d.data,safe=False)
    
@csrf_exempt
def model(req):
    if req.method=='GET':
        data=student.objects.all()
        d=model_serializers(data,many=True)
        return JsonResponse(d.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        data=model_serializers(data=d)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data)
        else:
            return JsonResponse(data.errors)