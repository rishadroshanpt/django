from django.urls import path
from . import views

urlpatterns=[
    path('',views.gallery_login),
    path('gallery_logout',views.gallery_logout),

    # ---------admin----------------

    path('admin_home',views.admin_home),
    path('view_img1/<id>',views.view_img1),
    path('users',views.users),

    # ------------user--------------

    path('register',views.register),
    path('user_home',views.user_home),
    path('add_img',views.add_img),
    path('my_img',views.my_img),
    path('dlt_img/<id>',views.dlt_img),
    path('view_img/<id>',views.view_img),



]