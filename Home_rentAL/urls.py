"""Home_rentAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path
from Shelter.views import home,about,contact,register,login,showdata
admin.site.site_header = "Shelter Admin"
admin.site.site_title = "Shelter Admin Portal"
admin.site.index_title = "Welcome to your SHELTER"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('login/', login,name='login'),
    path('register/', register,name='register'),
    path('showdata/', showdata,name='showdata'),
]
