from django.shortcuts import render
from .models import PsychoTest
from patient.models import Result

# Create your views here.


def test(request):
    test = PsychoTest.objects.all()
    context = {'listtests': test}
    return render(request, 'tests/test.html', context)


def spec(request, id):
    spec = PsychoTest.objects.get(test_id=id)
    con = Result.objects.filter(test=id).count()
    context = {'detail': spec,
               'count': con}
    return render(request, 'tests/sptest.html', context)




def testResult(request, id):
    # if request.method == "post":
        result = Result.objects.get(result_id= id)
        print(result.result_id)
        if result.test.test_id == 3:
            question = 22
        elif result.test.test_id == 2:
            question = 11
        else:
            question = 51

        countResult = []
        for x in range(1,question):
            a = int (request.POST.get('q'+str(x),False))
            countResult.append(a)
            print(a)
        res = sum(countResult)   
        print(res)
        result.test_result = res
        result.test_status = 1
        result.save()
        return render(request, 'blog/home.html')

# def test1(request):
#     anxResult = []
#     for x in range(1,51):
#         a = int (request.POST.get('q'+str(x),False))
#         anxResult.append(a)
#     result = sum(anxResult)   
#     print(result)
#     return render(request,'tests/anxietyTest.html') 

# def iniDiag(request):
#     # diag = PsychoTest.objects.all()
#     # context = {'iniDiag' : diag }
#     return render(request,'tests/iniDiag.html') 


    
# def test2(request):
#     ocdResult = []
#     for x in range(1,11):
#         a = int (request.POST.get('q'+str(x),False))
#         ocdResult.append(a)
#     result = sum(ocdResult)   
#     print(result)
#     return render(request,'tests/ocdTest.html') 