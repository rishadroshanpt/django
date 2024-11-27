from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('course/<id>',views.course),
    
] 