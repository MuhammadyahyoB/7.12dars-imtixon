from django.contrib import admin
from . import models

# --- register ---------------------

admin.site.register(models.Staff)
admin.site.register(models.Attendance)
