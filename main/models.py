from django.db import models
from django.utils import timezone


class Staff(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return f"{self.f_name}"
    
class Attendance(models.Model):
    staff_arrive = models.DateTimeField(null=True, blank=True)
    staff_rising = models.DateTimeField(null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff.f_name + ' ' + self.staff.l_name}"
    

