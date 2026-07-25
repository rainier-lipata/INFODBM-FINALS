from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AvailabilitySerializer, MentorExpertiseSerializer
from .services import (get_mentor_schedule, get_mentor_dashboard,
                       get_mentor_availability, update_availability, assign_mentor_topic)


class MentorScheduleAPIView(APIView):

    def get(self, request, mentor_id):

        data = get_mentor_schedule(mentor_id)

        return Response(data)

class MentorDashboardAPIView(APIView):

    def get(self, request, mentor_id):

        data = get_mentor_dashboard(mentor_id)

        return Response(data)

class MentorAvailabilityAPIView(APIView):

    def get(self, request, mentor_id):

        data = get_mentor_availability(mentor_id)

        return Response(data)

class UpdateAvailabilityAPIView(APIView):

    def put(self, request, availability_id):

        serializer = AvailabilitySerializer(data=request.data)

        if serializer.is_valid():

            update_availability(
                availability_id,
                serializer.validated_data
            )

            return Response(
                {
                    "message": "Availability updated successfully."
                }
            )

        return Response(
            serializer.errors,
            status=400
        )

class MentorExpertiseAPIView(APIView):

    def post(self, request):

        serializer = MentorExpertiseSerializer(data=request.data)

        if serializer.is_valid():

            message = assign_mentor_topic(
                serializer.validated_data
            )

            return Response(
                {
                    "message": message
                },
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )