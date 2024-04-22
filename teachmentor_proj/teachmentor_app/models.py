from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    book_link = models.URLField(blank=True)
    video_link = models.URLField(blank=True)
    def __str__(self):
        return f"{self.course_name}, {self.price}"


class FeedBackMessage(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateField()

    def __str__(self):
        return f"Feedback from {self.name} at {self.date_sent})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    liked_courses = models.ManyToManyField('Course', related_name='liked_by')

    def __str__(self):
        return self.user.username

