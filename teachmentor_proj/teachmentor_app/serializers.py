from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedBackMessage
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'


