"""
URL configuration for loginsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# your_app/urls.py
from django.urls import path
from .views import register, user_login
from django.contrib import admin
from django.urls import path, include
from your_app.views import home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('your_app.urls')),
    path('', home, name='home'),
]

