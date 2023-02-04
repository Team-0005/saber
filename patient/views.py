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
from django.contrib import messages


def addPatient(request):
    try:
        psycho_email= request.session['psycho_email']
        print("you are in add patient page")
        psych = Psychologist.objects.get(p_email=psycho_email)
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
                              pt_birth_date=bdate, p_email=Psychologist.objects.get(p_email=psycho_email))
            if Patient.objects.filter(pt_phone_no=phone) and Patient.objects.filter(p_email=psycho_email):
                print("This is wrong")
                messages.error(request, "رقم هاتف المريض مخزّن مسبقًا")
                return render(request, 'patient/addPatient.html', context)
            else:
                print("add patient success")
                new_patient.save()
                context = {'patient' : new_patient}
                return render(request, 'diagnosis/iniDiag.html', context)

    except:
        pass
    



def list_of_patient(request):
    try:
        psycho_email= request.session['psycho_email']
        list = Result.objects.filter(pt__p_email__exact=psycho_email)
        psych = Psychologist.objects.get(p_email=psycho_email)
        search = ""
        if 'searchField' in request.GET:
            search = request.GET['searchField']
            if search:
               lookups = Q(pt__pt_name__icontains=search) | Q(pt__pt_phone_no__icontains=search)
               list = list.filter(lookups)
               if list.count() == 0:
                  messages.success(request,"لا يوجد مريض بهذا الإسم او الرقم")

                       
        context = {
          'list': list,
          'search': search,
          'psycho': psych
        }
        return render(request, 'patient/patientRec.html', context)
    except:
        pass

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
    if request.method == "POST":
       psych = Psychologist.objects.get(p_email=psycho_email)
       temp_pat = Patient.objects.get(pt_id=pt_id)
       temp_pat.pt_name =  request.POST['pt_name']
       temp_pat.pt_phone_no =  request.POST['pt_phone_no']
       temp_pat.pt_birth_date =  request.POST['pt_birth_date']
       temp_pat.pt_edu_level =  request.POST['pt_edu_level']
       if temp_pat.pt_plan:
           temp_pat.pt_plan = request.POST['p_tr']
           
       temp_pat.save()
       messages.success(request,"تم حفظ التعديلات بنجاح")
    
    pat = Result.objects.get(pt__pt_id=pt_id)
    date = datetime.strptime(str(pat.pt.pt_birth_date), "%Y-%m-%d")
    today = date.today()
    dateBirth = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
    age = today.year - date.year
    sever=''
    if pat.test_result:
       sever = severity(pat.test.test_id, pat.test_result)

    context = {
        'pat': pat,
        'age': age,
        'sever': sever,
        'dateBirth': dateBirth,
        'psycho': psych
    }
    return render(request, 'patient/patientProfile.html',context)

def confResult(request, pt_id):
    pat = Result.objects.get(pt__pt_id=pt_id)
    sever = severity(pat.test.test_id, pat.test_result)
    context = {
        'pat': pat,
        'sever': sever,
    }
    return render(request, 'patient/conf_result.html',context)

def tretmentPlan(request, pt_id):
    pat = Result.objects.get(pt__pt_id=pt_id)
    temp_pat = Patient.objects.get(pt_id=pt_id)
    sever = severity(pat.test.test_id, pat.test_result)
    if request.method == "POST":
       psych = Psychologist.objects.get(p_email=psycho_email)
       temp_pat.pt_plan = request.POST['pt_plan']
       temp_pat.save()
       pat.test_status = 2
       pat.save()
       return list_of_patient(request)
       
    context = {
        'pat': pat,
        'sever': sever,
        'psycho': psych
    }
    return render(request, 'patient/tretment.html',context)
  
