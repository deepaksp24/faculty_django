from django.urls import path

from facultyData import views


urlpatterns = [
    path("", views.startPage),

    path("add_faculty_form/", views.addFacultyForm, name='addFacultyForm'),
    path("add_faculty/", views.addFaculty, name='addFaculty'),

    path("faculty_list/", views.featchFaculty, name='facultyList'),

    path("delete_faculty_form/", views.deleteFacultyForm, name='deleteFacultyForm'),
    path("delete_faculty/", views.deleteFaculty, name='deleteFaculty'),

    path("update_faculty_form/", views.updateFacultyForm, name='updateFacultyForm'),
    path("update_faculty/", views.updateFaculty, name='updateFaculty')
]
