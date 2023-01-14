"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views

urlpatterns = [
    path("", core_views.home, name='home'),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("tests/", include('tests.urls', namespace='tests')),
    path("patient/", include('patient.urls', namespace='patient')),
    path('signup/', core_views.signup, name='signup'),
    path('signin/', core_views.signin, name='signin'),
    path('profile/', core_views.profile, name='profile'),
    # path('<p_email>', core_views.profile, name='profile'),
    path('forget/', core_views.forget, name='forget'),
    path('reset/', core_views.reset, name='reset'),
<<<<<<< HEAD
    # path('signout', views.signout, name='signout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('signout', core_views.signout, name='signout'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

>>>>>>> 89c0987a5faadd3bf041be689e3fbbbbe19ad139
