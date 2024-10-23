from django.urls import path
from . import views
urlpatterns=[
    path('task1/<int:salary>/<int:year>',views.task1),
    path('task2/<city>',views.task2),
    path('task3/<int:num>',views.task3),
    path('task4/<int:ch>',views.task4),
    path('task5/<int:price>',views.task5),
    path('task6/<int:units>',views.task6),
    path('demo',views.demo)
    
    ]