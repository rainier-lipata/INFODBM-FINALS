from django.urls import path

from .views import (
    SearchMentorAPIView,
    StudentSessionsAPIView
)

urlpatterns = [

    path(
        "search-mentors/",
        SearchMentorAPIView.as_view(),
        name="search-mentors"
    ),

    path(
        "sessions/student/<int:student_id>/",
        StudentSessionsAPIView.as_view(),
        name="student-sessions"
    ),

]