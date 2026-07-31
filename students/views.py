from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import search_mentors, get_student_sessions


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


class StudentSessionsAPIView(APIView):

    def get(self, request, student_id):

        data = get_student_sessions(student_id)

        return Response(data)