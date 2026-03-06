
from django.urls import path
from . import views

urlpatterns = [

    path("",views.student_home,name="student-home"),
    path("add-student",views.add_student,name="add_student"),

]

