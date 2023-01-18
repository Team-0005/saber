from django.shortcuts import render

# Create your views here.


def iniDiag(request):
    # diag = PsychoTest.objects.all()
    # context = {'iniDiag' : diag }
    return render(request,'diagnosis/iniDiag.html')