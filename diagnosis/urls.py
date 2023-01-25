from django.urls import path
from . import views

app_name = 'diagnosis'

urlpatterns = [
    path('<pt_id>', views.iniDiag, name='iniDiag'),
    path('apptest/<int:id>/', views.apptest, name='apptest'),
    path('sendTest/<int:id>/', views.sendTest, name='sendTest'),
]