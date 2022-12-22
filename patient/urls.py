from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_of_patient, name='patient-list'),
    # path('', views.list_of_patient, name='patient-list'),
]