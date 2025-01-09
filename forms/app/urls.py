from django.urls import path
from . import views


urlpatterns=[
    path('',views.userForm),
    path('modelForm',views.modelForm)
]