from django.shortcuts import render
from django.http import HttpResponse
from .models import Admin
from .models import Psychologist
# Create your views here.




def home(request):
    return render(request, 'blog/home.html')  