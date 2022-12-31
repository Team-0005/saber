from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from .models import Patient
from .models import Result
from blog.models import Psychologist
from django.contrib import messages
from django.db.models import Q


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
    search = None
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
