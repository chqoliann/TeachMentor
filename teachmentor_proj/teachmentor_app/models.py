from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    book_link = models.URLField(blank=True)
    video_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.course_name}"


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


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.text} - {self.is_correct}"



class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.test.title}: {self.score}%"


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    test_result = models.ForeignKey(UserTestResult, on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

