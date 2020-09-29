from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from resume.models import Resume
from vacancy.models import Vacancy
from .forms import DescriptionForm

# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/signup/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            action = "/vacancy/new"
            entries = Vacancy.objects.all().filter(author=request.user)
        else:
            action = "/resume/new"
            entries = Resume.objects.all().filter(author=request.user)
        form = DescriptionForm(data=request.POST)
        return render(request, 'home.html', {'action': action, 'form': form, 'entries': entries})
    return render(request, 'home.html', {'action': ''})
