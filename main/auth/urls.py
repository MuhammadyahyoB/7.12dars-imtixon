from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('error/',views.error,name='error'),
    path('profil/',views.profil,name='profil'),
    path('setting/',views.setting,name='setting'),
    path('password-edit/',views.edit_password,name='edit_password'),

]