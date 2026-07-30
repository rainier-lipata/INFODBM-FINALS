from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import BookingRequestSerializer
from .services import create_booking, get_pending_requests, approve_booking, get_mentor_sessions, complete_session, get_student_sessions
from .models import BookingRequest



class CreateBookingAPIView(APIView):

    def post(self, request):

        print(request.data)

        serializer = BookingRequestSerializer(data=request.data)

        if serializer.is_valid():

            result = create_booking(serializer.validated_data)

            if result["success"]:
                return Response(
                    result,
                    status=status.HTTP_201_CREATED
                )

            return Response(
                result,
                status=status.HTTP_400_BAD_REQUEST
            )

class PendingRequestsAPIView(APIView):

    def get(self, request, mentor_id):
        data = get_pending_requests(mentor_id)

        return Response(data)

class ApproveBookingAPIView(APIView):

    def put(self, request, request_id):

        result = approve_booking(request_id)

        if result["success"]:

            return Response(result)

        return Response(
            {
                "message": result["Message"]
            },
            status=400
        )

class MentorSessionsAPIView(APIView):

    def get(self, request, mentor_id):

        data = get_mentor_sessions(mentor_id)

        return Response(data)

class CompleteSessionAPIView(APIView):

    def put(self, request, session_id):

        result = complete_session(session_id)

        if result["success"]:
            return Response(result)

        return Response(result, status=400)

class StudentSessionsAPIView(APIView):

    def get(self, request, student_id):

        data = get_student_sessions(student_id)

        return Response(data)