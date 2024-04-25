from django.contrib.auth import login, authenticate, logout
from .models import Course, UserProfile
from .forms import UserRegistrationForm, UserLoginForm, FeedbackForm
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.date_sent = timezone.now()
            feedback.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def feedback_success(request):
    return render(request, 'feedback_done.html')


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
            UserProfile.objects.create(user=new_user)
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


def like_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user_profile = request.user.userprofile
    user_profile.liked_courses.add(course)
    course.likes += 1
    course.save()
    return redirect('index')


@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    liked_courses = user_profile.liked_courses.all()
    return render(request, 'user_profile.html', {'user_profile': user_profile, 'liked_courses': liked_courses})


def course_details(request, course_id):
    courses = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details.html', {'course':courses})