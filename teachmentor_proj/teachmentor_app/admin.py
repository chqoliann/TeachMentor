from django.contrib import admin
from .models import Course, FeedBackMessage, UserProfile, Test, Question, Choice, UserTestResult

admin.site.register(Course)
admin.site.register(FeedBackMessage)
admin.site.register(UserProfile)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserTestResult)