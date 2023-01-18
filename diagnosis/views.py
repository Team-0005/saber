from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import keras
from keras.models import load_model
from blog.models import Psychologist

def iniDiag(request):
    try:
        psycho_email= request.session['psycho_email']
        print("you are in add patient page")
        psych = Psychologist.objects.get(p_email=psycho_email)
        context = {'psycho': psych}
        if request.method != "POST":
            return render(request,'diagnosis/iniDiag.html')
        else: 
            try:
                sleep_problems = request.POST['VII3']
                eating_problems = request.POST['VII1']
                conscience = request.POST['conscience']
                communication = request.POST['communication']
                face_features = request.POST['faceFeatures']
                talk = request.POST['talk']
                mood = request.POST['mood']
                behavior = request.POST['behavior']
                Fears = request.POST['pt_phone_no']
                thinking = request.POST['thinking']
                Focus = request.POST['Focus']
                Attention = request.POST['Attention']
                duration = request.POST['pt_gender']
                fields=[sleep_problems,eating_problems,conscience,communication,face_features,talk,mood,behavior,Fears,thinking,Focus,Attention,duration]
                if not None in fields:
                    #Datapreprocessing
                    fields = list(map(int, fields))
                    print(fields)
                    result = np.array(fields).reshape(1, 14) 
                    #Passing data to model & loading the model from disks
                    model_path = 'diagnosis\saber.h5'
                    classifier = keras.load(open(model_path, compile=False))
                    prediction = classifier.predict([result])[0]
                    print(prediction)
                    conf_score =  np.max(classifier.predict_proba([result]))*100
                    predictions = {
                        'error' : '0',
                        'message' : 'Successfull',
                        'prediction' : prediction,
                        'confidence_score' : conf_score
                    }
                else:
                    predictions = {
                        'error' : '1',
                        'message': 'Invalid Parameters'                
                    }
            except Exception as e:
                predictions = {
                    'error' : '2',
                    "message": str(e)
                }
        return render(request,'diagnosis/iniDiag.html')
    except:
        pass