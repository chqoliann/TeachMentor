from django.contrib.auth import login, authenticate, logout
from .models import Course, UserProfile, Test, Question, Choice
from .forms import UserRegistrationForm, UserLoginForm, FeedbackForm, CourseForm
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
    return render(request, 'index.html', {'courses': all_courses})


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
            return redirect('index')
        else:
            return render(request, 'register.html', {'user_form': user_form})
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
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    error = 'Account is disabled.'
                    return render(request, 'login.html', {'form': form, 'error': error})
            else:
                error = 'Invalid login credentials'
                return render(request, 'login.html', {'form': form, 'error': error})
        else:
            return render(request, 'login.html', {'form': form, 'errors': form.errors})
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
    course = get_object_or_404(Course, pk=course_id)
    test = Test.objects.filter(course=course).first()  # Получаем тест для данного курса
    return render(request, 'course_details.html', {'course': course, 'test': test})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def view_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    choices_for_questions = {}
    for question in questions:
        choices = Choice.objects.filter(question=question)
        choices_for_questions[question] = choices
    return render(request, 'test.html', {'test': test, 'questions': questions, 'choices_for_questions': choices_for_questions} )


def process_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    user = request.user
    correct_answers_count = 0
    total_questions = Question.objects.filter(test=test).count()

    if request.method == 'POST':
        if total_questions > 0:
            for question in Question.objects.filter(test=test):
                choice_id = request.POST.get(f'question_{question.id}', None)
                if choice_id is not None:
                    choice = get_object_or_404(Choice, pk=choice_id)
                    if choice.is_correct:
                        correct_answers_count += 1

            percentage_correct = (correct_answers_count / total_questions) * 100
        else:
            percentage_correct = 0

        selected_choices = {}
        for key in request.POST:
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                choice_id = request.POST[key]
                selected_choices[question_id] = get_object_or_404(Choice, pk=choice_id)

        return render(request, 'test_result.html', {
            'correct_answers_count': correct_answers_count,
            'total_questions': total_questions,
            'percentage_correct': percentage_correct,
            'selected_choices': selected_choices,
        })

    else:
        return redirect('test', test_id=test_id)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

