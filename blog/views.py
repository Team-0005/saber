from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Admin
from .models import Psychologist
from django.contrib import messages
# Create your views here.




def home(request):
    return render(request, 'blog/home.html')  



def signup(request):
    print("hello from submittion button")
    if request.method == "POST":
        p_email = request.POST['p_email']
        p_password = request.POST['p_password']
        p_f_name = request.POST['p_f_name']
        p_l_name = request.POST['p_l_name']
        p_phone_no = request.POST['p_phone_no']
        current_job_title = request.POST['current_job_title']
        scfhs_no = request.POST.get('scfhs_no',False)
        req_status = 0
        psycho = Psychologist(p_email=p_email,p_password=p_password,p_f_name=p_f_name,p_l_name=p_l_name,p_phone_no=p_phone_no,current_job_title=current_job_title,
        scfhs_no=scfhs_no,req_status=req_status)
        
        if Psychologist.objects.filter(p_email=p_email) or Psychologist.objects.filter(scfhs_no=scfhs_no):
            messages.error(request,"الإيميل أو رقم الرخصة مسجّل في سابر مسبقًا")
            print("This is wrong")
            return render(request, 'blog/home.html') 
        else :
            print("create account success")
            psycho.save()
            return render(request, 'blog/home.html') 

            
     



            

        # psycho = Psychologist.objects.create_user(p_email,p_password,p_f_name ,p_l_name,p_phone_no, current_job_title,scfhs_no ,req_status)

       

        
    
  

def test(request):
     return render(request, 'blog/Spetestinfo.html') 

def signin(request):
    return render(request, 'blog/home.html')

def signout(request):
    pass