from django.db import models

# Create your models here.

class Courses(models.Model):
    name=models.TextField()
    image=models.FileField()
    dis=models.TextField()
    overview=models.TextField()
    topic=models.TextField()
    batch=models.TextField()

class enquiry(models.Model):
    name=models.TextField()
    mobile=models.IntegerField()
    email=models.EmailField()
    msg=models.TextField()