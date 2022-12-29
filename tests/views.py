from django.shortcuts import render
from .models import PsychoTest
from patient.models import Result

# Create your views here.
def test(request):
    test = PsychoTest.objects.all()
    context = {'listtests' : test }
    return render(request,'tests/test.html',context)  
   
def spec(request , id):
    spec = PsychoTest.objects.get(test_id=id)
    con = Result.objects.filter(test=id).count()
    context = {'detail' : spec ,
               'count' : con }
    return render(request,'tests/sptest.html',context) 

def iniDiag(request):
    # diag = PsychoTest.objects.all()
    # context = {'iniDiag' : diag }
    return render(request,'tests/iniDiag.html') 

def test1(request):
    ocdResult = []
    for x in range(1,11):
        a = int (request.POST.get('q'+str(x),False))
        ocdResult.append(a)
    result = sum(ocdResult)   
    print(result)
    return render(request,'tests/ocdTest.html') 