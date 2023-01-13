from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path('<p_email>', views.list_of_patient, name='ptlist'),
    # path('addpt/<p_email>', views.addPatient, name='addpt'),
    path('addpt/', views.addPatient, name='addpt'),
    path('<pt_id>/', views.patientProf , name='patientProfile'),
    path('confResult/<pt_id>/', views.confResult , name='confResult'),
    path('tretmentPlan/<pt_id>/', views.tretmentPlan , name='tretmentPlan'),
]
