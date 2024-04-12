from django.contrib import admin
from django.urls import path, include  # Importing include for including app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teachmentor_app.urls')),  # Including teachmentor_app URLs
]
