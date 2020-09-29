"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView
from .views import menu, signin, signup, home
from vacancy.views import vacancies, new_vacancy
from resume.views import resumes, new_resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('login', signin, name='login'),
    path('signup', signup, name='signup'),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('vacancies/', vacancies, name='vacancies'),
    path('vacancy/new', new_vacancy, name='new_vacancy'),
    path('resumes/', resumes, name='resumes'),
    path('resume/new', new_resume, name='new_resume'),
    path('home', home, name='home'),
    path('home/', RedirectView.as_view(url='/home'))
]
