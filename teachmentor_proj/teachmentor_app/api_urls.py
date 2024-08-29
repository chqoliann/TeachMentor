from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'course', api_views.CourseViewSet)
router.register(r'fbm', api_views.FeedBackMessageViewSet)
router.register(r'uprofile', api_views.UserProfileViewSet)
router.register(r'test', api_views.TestViewSet)
router.register(r'question', api_views.QuestionViewSet)
router.register(r'choice', api_views.ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
