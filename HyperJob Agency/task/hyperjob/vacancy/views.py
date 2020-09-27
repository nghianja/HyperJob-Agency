from django.shortcuts import render
from .models import Vacancy

# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def vacancies(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancy_list})
