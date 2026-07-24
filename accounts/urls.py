from django.urls import path
from .views import (
    RegisterStudentAPIView,
    RegisterMentorAPIView,
    LoginAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [

    path(
        "register/student/",
        RegisterStudentAPIView.as_view()
    ),

    path(
        "register/mentor/",
        RegisterMentorAPIView.as_view()
    ),

    path(
        "login/",
        LoginAPIView.as_view(),
        name="login"
    ),

    path(
        "profile/<int:user_id>/",
        UpdateProfileAPIView.as_view(),
        name="update-profile"
    ),



]