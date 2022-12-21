from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_of_patient, name='add-patient'),
    # path('', views.list_of_patient, name='patient-list'),
]