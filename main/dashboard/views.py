from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth:login')
def index(request):
    """ index dashboard"""
    context = {}
    return render(request, 'dashboard/index.html', context)


# ----- staf list create  update --------------------------------
 
#  >>>> staf list <<<
@login_required(login_url='auth:login')
def staf_list(request):
    """ staf list """
    queryset = models.Staff.objects.all()
    context = {
          'queryset':queryset
    }
    return render(request, 'dashboard/staf/list.html', context)


# >>>>>> staf create <<<<
@login_required(login_url='auth:login')
def staf_create(request):
    """ staf create"""
    context = {}
    if request.method == 'POST':
        try:
            staf = models.Staff.objects.create(
                f_name = request.POST['f_name'],
                l_name = request.POST['l_name'],
                phone = request.POST['phone'],
                email = request.POST['email'],
                avatar = request.FILES.get('avatar'),
            )
            messages.success(request, 'Staffni  muvoffaqiyatli yaratildi')
        except:
            messages.error(request, 'stafni  yaratishda xatolik')
        return redirect('dashboard:staf_list')
    return render(request, 'dashboard/staf/create.html', context)


# >>>>>>>  staf update <<<<<<< 
@login_required(login_url='auth:login')
def staf_update(request, id):
    """ staf update """
    queryset = models.Staff.objects.get(id=id)
    context = {
          'queryset':queryset
    }
    if request.method == 'POST':
        try:
            queryset.f_name = request.POST['f_name']
            queryset.l_name = request.POST['l_name']
            queryset.phone = request.POST['phone']
            queryset.email = request.POST['email']
            if request.FILES.get('avatar'):    
                queryset.avatar = request.FILES.get('avatar')
            messages.success(request, 'stafni muvafiqiyatli ozgartirildi')
            queryset.save()
            return redirect('dashboard:staf_list')
        except:
            messages.error(request, 'stafni o`zgartirishda xatolik')
    return render(request, 'dashboard/staf/update.html', context)


#>>>>>  staf delete <<<<<
@login_required(login_url='auth:login')
def staf_delete(request, id):
    """ staf delete """
    try:
        staf = models.Staff.objects.get(id=id)
        messages.success(request, 'staffni  muvoffaqiyatli o`chirildi')
        staf.delete()
        return redirect('dashboard:staf_list')
    except:
        messages.error(request, 'stafni o`chirishda xatolik')
        return redirect('dashboard:staf_list')
    

def Attendance_list(request):
    """ Attendance list """
    queryset = models.Attendance.objects.all()
    context = {
          'queryset':queryset
    }
    return render(request, 'dashboard/attendance/list.html', context)
    