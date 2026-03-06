
from django.urls import path
from . import views

urlpatterns = [

    path("",views.student_home),
    path("add-student",views.add_student)

]

