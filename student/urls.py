
from django.urls import path
from . import views

urlpatterns = [

    path("",views.student_home,name="student-home"),
    path("add-student",views.add_student,name="add_student"),
    path("delete-student/<int:pk>",views.delete_student,name="delete-student"),
    path("edit-student/<int:pk>",views.edit_student,name="edit-student")

]

