from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(default="2000-01-01")
    gender=models.CharField(max_length=10,default="male")
    student_class=models.CharField(max_length=20,default="nursery")
    email=models.EmailField()
    phone=models.CharField(max_length=14,default="not provided")
    parent_name=models.CharField(max_length=100,default="not provided")
    address=models.TextField(default="not provided", max_length=500)

