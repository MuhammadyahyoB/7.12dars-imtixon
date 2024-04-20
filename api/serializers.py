from rest_framework.serializers import ModelSerializer
from main.models import Staff
from main.models import Attendance

class StaffSerializerList(ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'f_name', 'l_name']


class StaffSerializerDetail(ModelSerializer):
    class Meta:
        model = Staff
        fields = ['__all__']

class AttendanceSerializerCreate(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['__all__']