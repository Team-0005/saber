from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('', views.signup, name='blog-signup'),
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]