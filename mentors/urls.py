from django.urls import path

from .views import (MentorScheduleAPIView, MentorDashboardAPIView,
                    MentorAvailabilityAPIView, UpdateAvailabilityAPIView,
                    MentorExpertiseAPIView)

urlpatterns = [

    path(
        "schedule/<int:mentor_id>/",
        MentorScheduleAPIView.as_view(),
        name="mentor-schedule"
    ),

    path(
    "dashboard/<int:mentor_id>/",
        MentorDashboardAPIView.as_view(),
        name="mentor-dashboard"
    ),

    path(
        "availability/<int:mentor_id>/",
        MentorAvailabilityAPIView.as_view(),
        name="mentor-availability"
    ),


    path(
    "availability/update/<int:availability_id>/",
    UpdateAvailabilityAPIView.as_view(),
    name="update-availability"
    ),

    path(
    "expertise/",
    MentorExpertiseAPIView.as_view(),
    name="mentor-expertise"
    ),
]