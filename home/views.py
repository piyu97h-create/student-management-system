from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home/home.html")

def About(request):
    return render(request,"home/about.html")

def Courses(request):
    return render(request,"home/courses.html")