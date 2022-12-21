from django.shortcuts import render

# Create your views here.
def addPatient(request):
    return render(request, 'patient/addPatient.html')  
    

def list_of_patient(request):
    return render(request, 'patient/patientRec.html')  