from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home/home.html")

#this is the home page of the project
def home(request):
    return render(request,"home/home.html")
