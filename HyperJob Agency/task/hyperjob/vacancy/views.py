from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from hyperjob.forms import DescriptionForm
from .models import Vacancy


def vacancies(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancy_list})


def new_vacancy(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = DescriptionForm(data=request.POST)
            if form.is_valid():
                description = form.cleaned_data['description']
                vacancy = Vacancy(description=description, author=request.user)
                vacancy.save()
            return redirect('/home/')
    raise PermissionDenied
