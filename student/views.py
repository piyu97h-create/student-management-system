from django.shortcuts import render, redirect
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
        return redirect ("student-home")

    return render(request,"student/add_student.html")

def delete_student(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect("student-home")

def edit_student(request,pk):
    student=Student.objects.get(id=pk)

    if request.method=="POST":
        student.name=request.POST.get("input_name")
        student.email=request.POST.get("input_email")
        student.phone=request.POST.get("input_phone")
        student.save()
        return redirect("student-home")

    data={
        "student":student
    }
    return render(request,"student/edit_student.html",data)