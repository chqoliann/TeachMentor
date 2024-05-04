from django.contrib.auth import login, authenticate, logout
from .models import Course, UserProfile, Test, Question, Choice, UserAnswer, UserTestResult
from .forms import UserRegistrationForm, UserLoginForm, FeedbackForm, CourseForm
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def feedback_view_ru(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.date_sent = timezone.now()
            feedback.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'ru/feedback_ru.html', {'form': form})


def feedback_success_ru(request):
    return render(request, 'ru/feedback_done_ru.html')


def index_ru(request):
    all_courses = Course.objects.all()
    query = request.GET.get('q')
    if query:
        all_courses = all_courses.filter(course_name__icontains=query)
    return render(request, 'ru/index_ru.html', {'courses':all_courses})


def about_ru(request):
    return render(request, 'ru/about_ru.html')


def register_ru(request):
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
    return render(request, 'ru/register_ru.html', {'user_form': user_form})


def user_login_ru(request):
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
                return render(request, 'ru/login_ru.html', {'form': form, 'error': error})
    else:
        form = UserLoginForm()
    return render(request, 'ru/login.html_ru', {'form': form})


def user_logout_ru(request):
    logout(request)
    return redirect('/')


def register_done_ru(request):
    return render(request, 'ru/register_done_ru.html')


def like_course_ru(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user_profile = request.user.userprofile
    user_profile.liked_courses.add(course)
    course.likes += 1
    course.save()
    return redirect('index')


@login_required
def user_profile_ru(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    liked_courses = user_profile.liked_courses.all()
    return render(request, 'ru/user_profile_ru.html', {'user_profile': user_profile, 'liked_courses': liked_courses})


def course_details_ru(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    test = Test.objects.filter(course=course).first()  # Получаем тест для данного курса
    return render(request, 'ru/course_details_ru.html', {'course': course, 'test': test})


def add_course_ru(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'ru/add_course_ru.html', {'form':form})


def view_test_ru(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    choices_for_questions = {}
    for question in questions:
        choices = Choice.objects.filter(question=question)
        choices_for_questions[question] = choices
    return render(request, 'ru/test_ru.html', {'test': test, 'questions': questions, 'choices_for_questions': choices_for_questions} )


def process_test_ru(request, test_id):
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

        return render(request, 'ru/test_result_ru.html', {
            'correct_answers_count': correct_answers_count,
            'total_questions': total_questions,
            'percentage_correct': percentage_correct,
            'selected_choices': selected_choices,
        })

    else:
        return redirect('test', test_id=test_id)

def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language == 'ru':
            return redirect('teachmentor_ru_app:index')
        elif language == 'en':
            return redirect('teachmentor_app:index')
    return redirect('teachmentor_app:index')
