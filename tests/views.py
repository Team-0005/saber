from django.shortcuts import render
from .models import PsychoTest
from patient.models import Result
from blog.models import Psychologist

# Create your views here.


def test(request):
     try:
        psycho_email= request.session['psycho_email']
        test = PsychoTest.objects.all()
        psych = Psychologist.objects.get(p_email=psycho_email)
        context = {'listtests': test,
                'psycho': psych}
        return render(request, 'tests/test.html', context)
     except:
        pass

def spec(request, id):
    try:
        psycho_email= request.session['psycho_email']
        spec = PsychoTest.objects.get(test_id=id)
        con = Result.objects.filter(test=id).count()
        psych = Psychologist.objects.get(p_email=psycho_email)
        context = {'detail': spec,
               'count': con,
               'psycho': psych
               
               }
        return render(request, 'tests/sptest.html', context)
    except:
        pass



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
        return render(request, 'tests/test_done.html')

