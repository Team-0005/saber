from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tests'

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:id>', views.spec, name='spectest'),
    path('iniDiag/', views.iniDiag, name='iniDiag'),
    path('test1/', views.test1, name='ocdTest'),
    path('test2/', views.test2, name='depTest'),
    path('test3/', views.test3, name='anxTest'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
