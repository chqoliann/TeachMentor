from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_name}, {self.price}"

