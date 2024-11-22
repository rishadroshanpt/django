from rest_framework import serializers
from .models import *

class usr_serializers(serializers.Serializer):
    roll_no=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'