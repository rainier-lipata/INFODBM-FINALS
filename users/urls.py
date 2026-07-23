from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path(
        "student-dashboard/",
        views.student_dashboard,
        name="student_dashboard"
    ),
    path(
        "mentor-dashboard/",
        views.mentor_dashboard,
        name="mentor_dashboard"
    ),
]