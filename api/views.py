from main.models import Staff, Attendance
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from django.utils import timezone

# >>>>> staf list <<<<<
@api_view(['GET'])
def  staff_list(request):
    """ staf list """
    data = Staff.objects.all()
    serializer = serializers.StaffSerializerList(data, many=True) # json ga otdi 

    return Response(serializer.data)


# >>>>> staff detail <<<<<
@api_view(['GET'])
def  staff_detail(request, id):
    """ staf list """
    data = Staff.objects.get(id=id) # python
    serializer = serializers.StaffSerializerDetail(data, many=False) # json ga otdi 

    return Response(serializer.data)


@api_view(['POST'])
def attendance_create(request):
    """ Attendance create"""
    serializer = serializers.AttendanceSerializerCreate(data=request.data)
    if serializer.is_valid():
        staff =serializer.validated_data.get('staff')
        staff_arrive = serializer.validated_data.get('staff_arrive')
        staff_rising = serializer.validated_data.get('staff_rising')

        if  not staff_arrive:
            staff_arrive = timezone.now()
            serializer.validated_data['staff_arrive'] = staff_arrive
        
        last_attendance = Attendance.objects.filter(staff=staff).last()

        if last_attendance and not staff_rising:
            staff_rising = timezone.now()
            serializer.validated_data['staff_rising'] = staff_rising
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)