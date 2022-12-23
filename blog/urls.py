from django.urls import path
from . import views 


app_name='blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    # path('#', views.forget, name='forgetPass'),
    # path('signout', views.signout, name='signout'),
]