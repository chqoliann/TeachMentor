from django.urls import path
from .views import feedback_success_ru,feedback_view_ru, index_ru, about_ru, user_login_ru, user_logout_ru, register_ru, register_done_ru, like_course_ru, user_profile_ru, course_details_ru, add_course_ru, process_test_ru, view_test_ru, change_language

app_name = 'teachmentor_ru_app'

urlpatterns = [
    path('', index_ru, name='index_ru'),
    path('about/', about_ru, name='about_ru'),
    path('login/', user_login_ru, name='login_ru'),
    path('logout/', user_logout_ru, name='logout_ru'),
    path('register/', register_ru, name='register_ru'),
    path('register/done/', register_done_ru, name='register_done_ru'),
    path('feedback/', feedback_view_ru, name='feedback_ru'),
    path('feedback/success', feedback_success_ru, name='feedback_success_ru'),
    path('like/<int:course_id>/', like_course_ru, name='like_course_ru'),
    path('user/profile/', user_profile_ru, name='user_profile_ru'),
    path('course_details/<int:course_id>/', course_details_ru, name='course_details_ru'),
    path('add_course/', add_course_ru, name='add_course_ru'),
    path('test/<int:test_id>/', view_test_ru, name='test_ru'),
    path('test/<int:test_id>/process/', process_test_ru, name='process_test_ru'),
    path('change-language/', change_language, name='change_language_ru')
]

