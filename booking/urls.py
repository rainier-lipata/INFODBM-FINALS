from django.urls import path

from .views import CreateBookingAPIView, PendingRequestsAPIView, ApproveBookingAPIView

urlpatterns = [

    path(
        "create/",
        CreateBookingAPIView.as_view(),
        name="create-booking"
    ),

    path(
    "pending/",
    PendingRequestsAPIView.as_view(),
    name="pending-requests"
    ),

    path(
    "approve/<int:request_id>/",
    ApproveBookingAPIView.as_view(),
    name="approve-booking"
    ),
]