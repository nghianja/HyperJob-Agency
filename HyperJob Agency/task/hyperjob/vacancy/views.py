from django.shortcuts import render
from .models import Vacancy


def vacancies(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancy_list})
