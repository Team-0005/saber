from django.urls import path
from . import views 


app_name='blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('<p_email>', views.profile, name='profile'),
    path('forget/', views.forget, name='forget'),
    path('reset/', views.reset, name='reset'),
    # path('signout', views.signout, name='signout'),
]