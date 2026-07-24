from django.urls import path

from .views import (
    SearchMentorAPIView,
)

urlpatterns = [

    path(
        "search-mentors/",
        SearchMentorAPIView.as_view(),
        name="search-mentors"
    ),

]