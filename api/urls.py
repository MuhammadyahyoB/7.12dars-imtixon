from .import views
from django.urls import path

urlpatterns = [
    path('staff/list', views.staff_list),
    path('staff/detail/<int:id>/', views.staff_detail),
    path('attendance/create/', views.attendance_create),
]