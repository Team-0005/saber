from django.shortcuts import render
from .models import PsychoTest

# Create your views here.
def test(request):
    test = PsychoTest.objects.all()
    context = {'listtests' : test }
    return render(request,'tests/test.html',context)  
   
def spec(request):
    return render(request,'tests/sptest.html') 