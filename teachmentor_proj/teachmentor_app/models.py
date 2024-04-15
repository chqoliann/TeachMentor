from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField()
    def __str__(self):
        return f"{self.course_name}, {self.price}"


class FeedBackMessage(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateField()

    def __str__(self):
        return f"Feedback from {self.name} at {self.date_sent})"


