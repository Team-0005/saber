from django.shortcuts import render
from django.shortcuts import redirect
import numpy as np
import keras
from keras.models import load_model
from blog.models import Psychologist
from bs4 import BeautifulSoup
from patient.models import Result
model_path = 'diagnosis\saber.h5'
model = load_model(model_path, compile=False)
disorder = ["desperation","anxiety","OCD"]
fields=[]

def iniDiag(request,pt_id):
    try:
        psycho_email= request.session['psycho_email']
        if  request.method == "POST":
            print("prediction start")
            Datapreprocessing('eating_problems',request.POST['eating_problems'])
            Datapreprocessing('sleep_problems',request.POST['sleep_problems'])
            Datapreprocessing('conscience',request.POST['conscience'])
            Datapreprocessing('communication',request.POST['communication'])
            Datapreprocessing('faceFeatures',request.POST['faceFeatures'])
            Datapreprocessing('talk',request.POST['talk'])
            Datapreprocessing('mood',request.POST['mood'])
            Datapreprocessing('behavior',request.POST['behavior'])
            Datapreprocessing('thinkingObject',request.POST['thinkingObject'])
            Datapreprocessing('thinking',request.POST['thinking'])
            Datapreprocessing('Focus',request.POST['Focus'])
            Datapreprocessing('Attention',request.POST['Attention'])
            Datapreprocessing('orientation',request.POST['orientation'])
            preds = model.predict([fields])[0] 
            label = disorder[preds.argmax()]
            print(fields)
            print(label)
            if label == "anxiety":
                the_id = 1
            elif label == "OCD":
                the_id = 2
            elif label == "desperation":
                the_id = 3
            
            fields.clear()
            save_result = Result( pt_id = pt_id , fk_diagnosis_id=the_id , test_id=the_id , test_status=0)
            save_result.save()
            print("add result success")
            psych = Psychologist.objects.get(p_email=psycho_email)
            context = {'patient': save_result}
            print(save_result.pt.pt_id)
            return redirect('diagnosis:apptest', id=save_result.pt.pt_id)
            
        return render(request,'diagnosis/iniDiag.html')
    except:
        pass
        return render(request, 'blog/home.html')



def Datapreprocessing(name,value):
    soup = BeautifulSoup(open('diagnosis/templates/diagnosis/iniDiag.html','r'),"html.parser")
    select = soup.find(attrs={'name':name})
    for option in select.find_all('option'):
         if value == option['value']:
            fields.append(1)
         else:
             fields.append(0)
    fields.pop()


def apptest(request, id):
        result = Result.objects.get(pt__pt_id= id)
        print(result.pt.pt_id)
        context = {
          'result': result,
        }

        return render(request, 'diagnosis/appro_test.html',context)





def sendTest(request, id):
    result = Result.objects.get(pt__pt_id= id)
    print(result.pt_id)
    context = {
      'result': result,
    }
    if(result.test_id == 1):
         return render(request, 'tests/anxietyTest.html',context)
    elif(result.test_id == 2):
          return render(request, 'tests/ocdTest.html',context)
    else:
         return render(request, 'tests/depressionTest.html',context)
 
    