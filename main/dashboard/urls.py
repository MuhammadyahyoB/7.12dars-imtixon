from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    
    path('', views.index),

    # -->>> staf create update list delete <<<---
    path('staf_list', views.staf_list, name='staf_list'),
    path('staf_create', views.staf_create, name='staf_create'),
    path('staf_update/<int:id>/', views.staf_update, name='staf_update'),
    path('staf_delete/<int:id>/', views.staf_delete, name='staf_delite'),
    path('attendance/list/', views.Attendance_list, name='Attendance_list'),

]