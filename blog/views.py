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
from email.message import EmailMessage
import smtplib
import random
# Create your views here.


def home(request):
    try:
        psycho_email= request.session['psycho_email']
        psych = Psychologist.objects.get(p_email=psycho_email)
        context = {'psycho': psych}
        return render(request, 'blog/psychologis.html', context)
    except:
        return render(request, 'blog/home.html')


def signup(request):
    print("you are in signup")
    if request.method == "POST":
        p_email = request.POST['p_email']
        p_password = request.POST['p_password']
        enc_pass = pbkdf2_sha256.encrypt(
            p_password, rounds=12000, salt_size=32)
        p_f_name = request.POST['p_f_name']
        p_l_name = request.POST['p_l_name']
        p_phone_no = request.POST['p_phone_no']
        current_job_title = request.POST['current_job_title']
        scfhs_no = request.POST.get('scfhs_no', False)
        req_status = 0
        scfhs_file = request.FILES['scfhs_file']
        psycho = Psychologist(p_email=p_email, p_password=enc_pass, p_f_name=p_f_name, p_l_name=p_l_name, p_phone_no=p_phone_no, current_job_title=current_job_title,
                              scfhs_no=scfhs_no, req_status=req_status, scfhs_file=scfhs_file)
        if pbkdf2_sha256.verify(p_password, enc_pass):
            print("tha pass encrypted success")
        else:
            print("tha pass encrypted faild")
        if Psychologist.objects.filter(p_email=p_email) or Psychologist.objects.filter(scfhs_no=scfhs_no):
            messages.error(
                request, "الإيميل أو رقم الرخصة مسجّل في سابر مسبقًا")
            print("This is wrong")
            return render(request, 'blog/signUp.html') 
        else:
            messages.success(request,"تم إرسال الطلب بنجاح")
            print("create account success")
            psycho.save()
            return render(request, 'blog/home.html')
    else:
          return render(request, 'blog/signUp.html')  

def signin(request):
    print("you are in signin")
    if request.method == "POST":
        p_email = request.POST['email']
        p_password = request.POST['password']

        if Psychologist.objects.filter(p_email=p_email):
            psych = Psychologist.objects.get(p_email=p_email)
            if pbkdf2_sha256.verify(p_password, psych.p_password):
                if psych.req_status == 1:
                    sendEmail(psych.p_email)
                    print("signin sucess")
                    passCodeSession= request.session['passCodeSession'] = 2
                    context = {'psycho': psych}
                    return render(request, 'blog/forgetPassCode.html',context)
                   # return render(request, 'blog/psychologis.html', context)
                else:
                    messages.error(request, "طلبك قيد المراجعة الرجاء انتظار الرد")
                    return render(request, 'blog/signIn.html')
            else:
                print("wrong password")
                messages.error(request, "كلمة المرور خاطئة")
                return render(request, 'blog/signIn.html')
        else:
            print("the email is not register")
            messages.error(request, "هذا الإيميل غير مسجّل في موقع سابر")
            return render(request, 'blog/signIn.html')
    else:
          return render(request, 'blog/signIn.html')      

def forget(request):
    print("you are in forget password")
    if request.method == "POST":
        p_email = request.POST.get('fp_email', False)
        if Psychologist.objects.filter(p_email=p_email):
            psych = Psychologist.objects.get(p_email=p_email)
            # sendEmail(psych.p_email)
            context = {'psycho': psych}
            passCodeSession= request.session['passCodeSession'] = 1
            return render(request, 'blog/forgetPassCode.html',context)
        else:
            messages.error(request, "هذا الإيميل غير مسجّل في موقع سابر")
            print("the email is not register")
            return render(request, 'blog/forgetPass.html')
    else:        
         return render(request, 'blog/forgetPass.html')

def reset(request,p_email):
    print("you are in reset password")
    if request.method == "POST":
        psych = Psychologist.objects.get(p_email=p_email)
        p_password = request.POST['password']
        enc_pass = pbkdf2_sha256.encrypt(
            p_password, rounds=12000, salt_size=32)
        psych.p_password = enc_pass
        psych.save()
        context = {'psycho': psych}
        print("password updated")
        messages.success(request,"تم تغيير كلمة المرور بنجاح")
        return render(request, 'blog/signIn.html',context)
    else:
        return render(request,'blog/changPass.html')


def sendEmail(p_email):
    n = random.randint(1000,9999)
    psych = Psychologist.objects.get(p_email=p_email)
    psych.p_code = n
    psych.save()
    user = "saber27.team@gmail.com"
    password = "xzvwkvysilwyxssw"
    msg = EmailMessage()
    msg.set_content("رمز التحقق الخاص بك هو : "+ str(n))
    msg['subject'] = "رمز التححق من سابِر "
    msg['to'] = p_email
    msg['from'] = user        
    print("correct email")
    server = smtplib.SMTP("smtp.gmail.com",25)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()



def passCode(request,p_email):

    if request.method == "POST":
        psych = Psychologist.objects.get(p_email=p_email)
        context = {'psycho': psych} 
        p_code = request.POST['p_code']
        if (psych.p_code == p_code):
            psych.p_code = None
            psych.save()
            context = {'psycho': psych}
            try:
                passCodeSession= request.session['passCodeSession'] 
                if(passCodeSession==1):
                    request.session.clear()
                    return render(request,'blog/changPass.html',context)
                else:
                    request.session.clear()
                    psycho_email= request.session['psycho_email'] = psych.p_email
                    return render(request, 'blog/psychologis.html', context)
            except:
                print("something wrong")
                return render(request,'blog/forgetPassCode.html',context)
                

        else:
            messages.error(request,"الكود المدخل غير صحيح الرجاء التأكد")
            return render(request,'blog/forgetPassCode.html',context)
    else: 
        sendEmail(p_email)
        psych = Psychologist.objects.get(p_email=p_email)
        context = {'psycho': psych}       
        return render(request, 'blog/forgetPassCode.html',context)


def profile(request):
    try:
        psycho_email= request.session['psycho_email']
        if request.method == "POST":
            temp_psycho = Psychologist.objects.get(p_email=psycho_email)
            if request.POST.get('email', False) != psycho_email:
                temp_email = request.POST.get('email', False)
                if Psychologist.objects.filter(p_email=temp_email):
                    print("this email already exisit")
                    messages.error(request,"هذا الإيميل مسجّل في سابِر مسبقًا")
                    context = {'information': temp_psycho}
                    return render(request, 'blog/profile.html', context)
                else:
                    change = True
            else:
                change = True
                if change:
                    temp_psycho.p_email = request.POST.get('email', False)
                    temp_psycho.p_f_name = request.POST['p_f_name']
                    temp_psycho.p_l_name = request.POST['p_l_name']
                    temp_psycho.p_phone_no = request.POST['p_phone_no']
                    temp_psycho.save()
                    context = {'information': temp_psycho}
                    messages.success(request,"تم حفظ التعديلات بنجاح")
                    return render(request, 'blog/profile.html', context)
                else:
                    messages.error(request,"هناك خطأ في البيانات المدخلة")
                    context = {'information': temp_psycho}
                    return render(request, 'blog/profile.html', context)
        else:
            psych = Psychologist.objects.get(p_email=psycho_email)
            context = {'information': psych}
            return render(request, 'blog/profile.html', context)

    except:
        pass    
    




def signout(request):
    request.session.clear()
    return render(request, 'blog/home.html')
