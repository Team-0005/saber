from django.urls import path
from . import views 

app_name= 'patient'
urlpatterns = [
    path('', views.list_of_patient, name='patient-list'),
    path('', views.addPatient, name='add-patient'),
]