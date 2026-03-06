
from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home,name="home"),
    path("about/", views.About,name="about"),
    path("courses/", views.Courses,name="courses"),
    path("students/", views.student_home,name="students"),

]

