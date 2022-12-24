from django.urls import path
from . import views 

app_name= 'patient'
urlpatterns = [
    path('', views.list_of_patient, name='ptlist'),
    path('addpt/<p_email>', views.addPatient, name='addpt'),
]