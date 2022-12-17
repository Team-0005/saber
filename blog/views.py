from django.shortcuts import render
from django.http import HttpResponse
from .models import Admin
from .models import Psychologist
from django.contrib import messages
# Create your views here.


def test(request):
     return render(request, 'blog/Spetestinfo.html')

def home(request):
    return render(request, 'blog/home.html')  

# def signup(request):
#     if request.method == "post":
#         print("This is post")
#         p_email = request.post['p_email']
#         p_password = request.post['p_password']
#         p_f_name = request.post['p_f_name']
#         p_l_name = request.post['p_l_name']
#         p_phone_no = request.post['p_phone_no']
#         current_job_title = request.post['current_job_title']
#         scfhs_no = request.post['scfhs_no']
#         # scfhs_file = request.post['p_email']
#         req_status = 0

#         if Psychologist.objects.filter(p_email=p_email) or Psychologist.objects.filter(scfhs_no=scfhs_no):
#             messages.error(request,"الإيميل أو رقم الرخصة مسجّل في سابر مسبقًا")
            

#         psycho = Psychologist.objects.create_user(p_email,p_password,p_f_name ,p_l_name,p_phone_no, current_job_title,scfhs_no ,req_status)

#         psycho.save()

#         messages.success(request,"تم إرسال الطلب بنجاح")
    
#     return render(request, 'blog/signup.html')

# def signin(request):
#     return render(request, 'blog/home.html')

# def signout(request):
#     pass