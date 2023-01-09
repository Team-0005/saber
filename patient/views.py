from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from .models import Patient
from .models import Result
from blog.models import Psychologist
from django.contrib import messages
from django.db.models import Q
from datetime import *


# Create your views here.
def addPatient(request, p_email):
    print("you are in add patient page")
    psych = Psychologist.objects.get(p_email=p_email)
    context = {'psycho': psych}
    if request.method != "POST":
        return render(request, 'patient/addPatient.html', context)
    else:
        name = request.POST['pt_name']
        bdate = request.POST['pt_birth_date']
        gender = request.POST.get('pt_gender', False)
        phone = request.POST['pt_phone_no']
        edu_level = request.POST['pt_edu_level']
        new_patient = Patient(pt_phone_no=phone, pt_name=name, pt_gender=gender, pt_edu_level=edu_level,
                              pt_birth_date=bdate, p_email=Psychologist.objects.get(p_email=p_email))
        if Patient.objects.filter(pt_phone_no=phone) and Patient.objects.filter(p_email=p_email):
            messages.error(request, "المرض مخزّن مسبقًا")
            print("This is wrong")
            return render(request, 'patient/addPatient.html', context)
        else:
            print("add patient success")
            new_patient.save()
            return render(request, 'blog/psychologis.html', context)


def list_of_patient(request, p_email):
    psy = Psychologist.objects.get(p_email=p_email)

    list = Result.objects.filter(pt__p_email__exact=p_email)
    search = ""
    if 'searchField' in request.GET:
        search = request.GET['searchField']
        if search:
            lookups = Q(pt__pt_name__icontains=search) | Q(pt__pt_phone_no__icontains=search)
            list = list.filter(lookups)
                       
    context = {
        'psy': psy,
        'list': list,
        'search': search
    }
    return render(request, 'patient/patientRec.html', context)

def severity(test, result):
    if test == 1:
        if result >= 0 and result <= 16:
            return 'لا يوجد قلق'
        elif result >= 17 and result <= 20:
            return 'قلق بسيط'
        elif result >= 21 and result <= 26:
            return 'قلق متوسط'
        elif result >= 27 and result <= 29:
            return 'قلق شديد'
        else:
            return 'قلق شديد جدا'

    elif test == 2:
        if result >= 0 and result <= 7:
            return 'وسواس خفيف جدا'
        elif result >= 8 and result <= 15:
            return 'وسواس خفيف'
        elif result >= 16 and result <= 23:
            return 'وسواس متوسط'
        elif result >= 24 and result <= 31:
            return 'وسواس ملحوظ'
        else:
            return 'وسواس شديد'
        
    else:
        if result >= 0 and result <= 9:
            return  'لا يوجد اكتئاب'
        elif result >= 10 and result <= 15:
            return 'اكتئاب بسيط'
        elif result >= 16 and result <= 23:
            return 'اكتئاب متوسط'
        elif result >= 24 and result <= 36:
            return 'اكتئاب شديد'
        else:
            return 'اكتئاب شديد جدا'


def patientProf(request, pt_id):
    pat = Result.objects.get(pt__pt_id=pt_id)
    date = datetime.strptime(str(pat.pt.pt_birth_date), "%Y-%m-%d")
    today = date.today()
    age = today.year - date.year
    sever=''
    if pat.test_result:
       sever = severity(pat.test.test_id, pat.test_result)
    
    context = {
        'pat': pat,
        'age': age,
        'sever': sever,
    }
    return render(request, 'patient/patientProfile.html',context)
  
