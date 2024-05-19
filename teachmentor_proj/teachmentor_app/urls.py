from django.urls import path
from .views import feedback_success,feedback_view, index, about, user_login, user_logout, register, register_done, like_course, user_profile, course_details, add_course, process_test, view_test


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('register/done/', register_done, name='register_done'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/success', feedback_success, name='feedback_success'),
    path('like/<int:course_id>/', like_course, name='like_course'),
    path('user/profile/', user_profile, name='user_profile'),
    path('course_details/<int:course_id>/', course_details, name='course_details'),
    path('add_course/', add_course, name='add_course'),
    path('test/<int:test_id>/', view_test, name='test'),
    path('test/<int:test_id>/process/', process_test, name='process_test'),
]

