from django.shortcuts import render
from .models import Student

# Create your views here.

def student_home(request):
    students_Data=Student.objects.all()

    data={
        "students_Data":students_Data
    }

    return render(request,"student/student_home.html",data)

def add_student(request):
    if request.method=="POST":
        student_name=request.POST.get("input_name")
        student_email=request.POST.get("input_email")
        student_phone=request.POST.get("input_phone")

        Student.objects.create(
            name=student_name,
            email=student_email,
            phone=student_phone
        )

    return render(request,"student/add_student.html")