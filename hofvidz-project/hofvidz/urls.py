"""
URL configuration for hofvidz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin, auth
from django.urls import path
#cannot just import views like that you need to 
from django.contrib.auth import views as auth_views

#
from halls import views
from django.conf.urls.static import static
from django.conf import settings
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name= 'home'),
    #auth paths 
    path('signup/',views.SignUp.as_view(),name= 'signup'),
    path('login/',auth.views.LoginView.as_view(),name= 'login'),
    path('logout/',auth.views.LogoutView.as_view(),name= 'logout'),
    
    
    
]
urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)