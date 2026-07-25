from django.urls import path

from .views import (
    SearchMentorAPIView,
    StudentSessionAPIView
)

urlpatterns = [

    path(
        "search-mentors/",
        SearchMentorAPIView.as_view(),
        name="search-mentors"
    ),



    path(
        "sessions/<int:student_id>/",
        StudentSessionAPIView.as_view(),
        name="student-sessions"
    ),

]