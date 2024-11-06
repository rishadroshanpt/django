from django.urls import path
from . import views
urlpatterns=[
    path('',views.arms_login),
    path('home',views.home),
    path('arms_logout',views.arms_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete)

]