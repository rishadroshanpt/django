from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.TextField()
    image=models.FileField()