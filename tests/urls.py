from django.urls import path
from . import views 

app_name='tests'

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:id>', views.spec, name='spectest'),
    path('iniDiag/', views.iniDiag, name='iniDiag'),
    path('test1/', views.test1, name='ocdTest'),
    path('test2/', views.test2, name='depTest'),

]