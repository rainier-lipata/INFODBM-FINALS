from django.urls import path

from .views import (login_page, student_dashboard, mentor_dashboard,)

urlpatterns = [

    path(
        "login/",
        login_page,
        name="login"
    ),

    path(
        "student-dashboard/",
        student_dashboard,
        name="student-dashboard"
    ),

    path(
        "mentor-dashboard/",
        mentor_dashboard,
        name="mentor-dashboard"
    ),

]