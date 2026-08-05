from django.urls import path

from .views import (CreateBookingAPIView, PendingRequestsAPIView, ApproveBookingAPIView,
                    MentorSessionsAPIView, CompleteSessionAPIView, StudentSessionsAPIView, AddAvailabilityAPIView, DeleteAvailabilityAPIView)

urlpatterns = [

    path(
        "create/",
        CreateBookingAPIView.as_view(),
        name="create-booking"
    ),

    path(
        "pending/<int:mentor_id>/",
        PendingRequestsAPIView.as_view(),
        name="pending-requests"
    ),

    path(
        "approve/<int:request_id>/",
        ApproveBookingAPIView.as_view(),
        name="approve-booking"
    ),

    path(
        "sessions/mentor/<int:mentor_id>/",
        MentorSessionsAPIView.as_view(),
        name="mentor-sessions"
    ),

    path(
        "sessions/complete/<int:session_id>/",
        CompleteSessionAPIView.as_view(),
        name="complete-session"
    ),

    path(
        "sessions/student/<int:student_id>/",
        StudentSessionsAPIView.as_view(),
        name="student-sessions"
    ),

    path(
    "availability/add/",
    AddAvailabilityAPIView.as_view()
    ),

    path(
    "availability/delete/<int:availability_id>/",
    DeleteAvailabilityAPIView.as_view()
    ),
]