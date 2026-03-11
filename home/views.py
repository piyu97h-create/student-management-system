from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home/home.html")

def About(request):
    return render(request,"home/about.html")

def Courses(request):
    courses_Data=courses.obejcts.all()
    courses_Data={
        "courses-data":courses_Data
    }
    return render(request,"home/courses.html",courses_Data)

def student_home(request):
    return render(request,"student/student_home.html") 
