from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from hyperjob.forms import DescriptionForm
from .models import Resume

# Create your views here.


def resumes(request):
    resume_list = Resume.objects.all()
    return render(request, 'resumes.html', {'resumes': resume_list})


def new_resume(request):
    if request.user.is_authenticated and not request.user.is_staff:
        if request.method == 'POST':
            form = DescriptionForm(data=request.POST)
            if form.is_valid():
                description = form.cleaned_data['description']
                resume = Resume(description=description, author=request.user)
                resume.save()
            return redirect('/home/')
    raise PermissionDenied
