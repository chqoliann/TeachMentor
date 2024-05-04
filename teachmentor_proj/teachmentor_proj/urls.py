from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teachmentor_app.urls')),
    path('', include('teachmentor_ru_app.urls'))
]
