from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Course
from .forms import UserRegistrationForm, UserLoginForm


def index(request):
    all_courses = Course.objects.all()
    query = request.GET.get('q')
    if query:
        all_courses = all_courses.filter(course_name__icontains=query)
    return render(request, 'index.html', {'courses':all_courses})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error = 'Invalid login credentials'
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def register_done(request):
    return render(request, 'register_done.html')