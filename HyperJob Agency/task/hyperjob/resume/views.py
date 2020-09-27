from django.shortcuts import render
from .models import Resume

# Create your views here.


def resumes(request):
    resume_list = Resume.objects.all()
    return render(request, 'resumes.html', {'resumes': resume_list})
