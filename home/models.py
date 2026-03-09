from django.db import models

# Create your models here.

class courses(models.Model):
    courseCode=models.CharField(max_length=10)
    courseName=models.CharField(max_length=100)
    instructor=models.CharField(max_length=100)
    credits=models.IntegerField()
    actions=models.CharField(max_length=100)
    def __str__(self):
        return self.courseName