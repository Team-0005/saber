from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from . import forms
from .models import Admin
from .models import Psychologist
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate
# Create your views here.



def home(request):
    return render(request, 'blog/home.html')  
    



def signup(request):
    print("you are in signup")
    if request.method == "POST":
        p_email = request.POST['p_email']
        p_password = request.POST['p_password']
        enc_pass = pbkdf2_sha256.encrypt(p_password, rounds=12000,salt_size=32)
        p_f_name = request.POST['p_f_name']
        p_l_name = request.POST['p_l_name']
        p_phone_no = request.POST['p_phone_no']
        current_job_title = request.POST['current_job_title']
        scfhs_no = request.POST.get('scfhs_no',False)
        req_status = 0
        scfhs_file = request.FILES['scfhs_file']
        psycho = Psychologist(p_email=p_email,p_password= enc_pass,p_f_name=p_f_name,p_l_name=p_l_name,p_phone_no=p_phone_no,current_job_title=current_job_title,
        scfhs_no=scfhs_no,req_status=req_status,scfhs_file=scfhs_file )
        if pbkdf2_sha256.verify(p_password,enc_pass):
            print("tha pass encrypted success")
        else:
            print("tha pass encrypted faild")
        if Psychologist.objects.filter(p_email=p_email) or Psychologist.objects.filter(scfhs_no=scfhs_no):
            messages.error(request,"الإيميل أو رقم الرخصة مسجّل في سابر مسبقًا")
            print("This is wrong")
            return render(request, 'blog/home.html')
        else :
            # messages.SUCCESS(request,"تم إرسال الطلب بنجاح")
            print("create account success")
            psycho.save()
            return render(request, 'blog/home.html') 



def signin(request):
     print("you are in signin")
     if request.method == "POST":
        p_email = request.POST['email']
        p_password = request.POST['password']

        if Psychologist.objects.filter(p_email=p_email):
            psych = Psychologist.objects.get(p_email=p_email)
            if pbkdf2_sha256.verify(p_password,psych.p_password):
                if psych.req_status== 1:
                    print("signin sucess")
                    context = {'psychologist' : psych }
                    return render(request, 'blog/psychologis.html')
                else:
                    print("not replaying yet")
                    return render(request, 'tests/test.html')
            else:
                print("wrongpassword")
                return render(request, 'blog/home.html')
        else:
            print("the email is not register")
            return render(request, 'blog/home.html', context)



        # Psychologist = authenticate(p_email=p_email,p_password= enc_pass)
        # if Psychologist is None:
        #     messages.error(request,"الإيميل أو كلمة المرور خاطئة")
        #     return render(request, 'blog/home.html')  
        # else:
        #     if Psychologist.reqstatus==0:
        #         messages.error(request,"لم يتم التحقق من طلبك بعد")
        #         return render(request, 'blog/home.html') 

# def forget(request):
#     print("you are in signin")
#     if request.method == "POST":
#         p_email = request.POST['p_email']
#         if Psychologist.objects.filter(p_email=p_email):
#             psych = Psychologist.objects.get(p_email=p_email)
#         else:
#             print("the email is not register")
#             return render(request, 'blog/home.html')
#     else:
#             print("the email is not register")
#             return render(request, 'blog/home.html')

#     return render(request, 'blog/home.html') 


# def signout(request):
#     pass