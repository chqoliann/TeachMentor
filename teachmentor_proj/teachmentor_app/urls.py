from django.urls import path
from .views import index, about, user_login, user_logout, register, register_done

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('register/done/', register_done, name='register_done'),
]