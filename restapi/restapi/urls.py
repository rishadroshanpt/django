"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usr_ser',views.usr_def_serializers),
    path('model',views.model),
    path('fun4/<d>',views.fun4),
    path('fun5',views.fun5),
    path('fun6/<d>',views.fun6),
    path('fun7',views.fun7.as_view()),
    path('fun8/<d>',views.fun8.as_view()),
    path('fun9',views.genericapiview.as_view()),
    path('fun10/<id>',views.update.as_view()),
]
