from django.contrib import admin
from .models import Course, FeedBackMessage, UserProfile

admin.site.register(Course)
admin.site.register(FeedBackMessage)
admin.site.register(UserProfile)