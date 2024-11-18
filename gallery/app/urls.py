from django.urls import path
from . import views

urlpatterns=[
    path('',views.gallery_login),
    path('gallery_logout',views.gallery_logout),

    # ---------admin----------------

    path('admin_home',views.admin_home),

    # ------------user--------------

    path('register',views.register),
    path('user_home',views.user_home),
    path('add_img',views.add_img),

]