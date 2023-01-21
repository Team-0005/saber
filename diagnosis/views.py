from django.shortcuts import render
import numpy as np
import keras
from keras.models import load_model
from blog.models import Psychologist

model_path = 'diagnosis\saber.h5'
model = load_model(model_path, compile=False)
disorder = ["desperation","anxiety","OCD"]
fields=[]

def iniDiag(request):
    try:
        if  request.method == "POST":
            print("predction start")
            Datapreprocessing('eating_problems',request.POST['eating_problems'],4)
            Datapreprocessing('sleep_problems',request.POST['sleep_problems'],3)
            Datapreprocessing('conscience',request.POST['conscience'],4)
            Datapreprocessing('communication',request.POST['communication'],3)
            Datapreprocessing('faceFeatures',request.POST['faceFeatures'],4)
            Datapreprocessing('talk',request.POST['talk'],4)
            Datapreprocessing('mood',request.POST['mood'],4)
            Datapreprocessing('behavior',request.POST['behavior'],4)
            Datapreprocessing('thinkingObject',request.POST['thinkingObject'],4)
            Datapreprocessing('thinking',request.POST['thinking'],4)
            Datapreprocessing('Focus',request.POST['Focus'],3)
            Datapreprocessing('Attention',request.POST['Attention'],4)
            Datapreprocessing('orientation',request.POST['orientation'],3)
            preds = model.predict([fields])[0] 
            label = disorder[preds.argmax()]
            print(label)
            fields.clear()
        return render(request,'diagnosis/iniDiag.html')
    except:
        pass
        return render(request,'diagnosis/iniDiag.html')



def Datapreprocessing(option,value,n):
    for i in range(1,n):
        if value == (option+"-"+str(i)):
            fields.append(1)
        else:
            fields.append(0)