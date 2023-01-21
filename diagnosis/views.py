from django.shortcuts import render
import numpy as np
import keras
from keras.models import load_model
from blog.models import Psychologist
from bs4 import BeautifulSoup

model_path = 'diagnosis\saber.h5'
model = load_model(model_path, compile=False)
disorder = ["desperation","anxiety","OCD"]
fields=[]

def iniDiag(request):
    try:
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
            fields.clear()
        return render(request,'diagnosis/iniDiag.html')
    except:
        pass
        return render(request,'diagnosis/iniDiag.html')



def Datapreprocessing(name,value):
    soup = BeautifulSoup(open('diagnosis/templates/diagnosis/iniDiag.html','r'),"html.parser")
    select = soup.find(attrs={'name':name})
    for option in select.find_all('option'):
         if value == option['value']:
            fields.append(1)
         else:
             fields.append(0)
    fields.pop()