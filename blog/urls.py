from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('signup/', views.signup, name='signup'),
    path('spetestinfo/', views.test, name= 'spetestinfo'),
    # path('', views.signin, name='signin'),
    # path('signout', views.signout, name='signout'),
    path('listtest/', views.listtest, name= 'listtest'),
]