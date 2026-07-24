from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import search_mentors


class SearchMentorAPIView(APIView):

    def get(self, request):

        topic = request.GET.get("topic")

        if not topic:

            return Response(
                {
                    "message": "Please provide a topic."
                },
                status=400
            )

        mentors = search_mentors(topic)

        return Response(mentors)
