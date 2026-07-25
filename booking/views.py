from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookingRequestSerializer
from .services import create_booking, get_pending_requests, approve_booking



class CreateBookingAPIView(APIView):

    def post(self, request):

        print(request.data)

        serializer = BookingRequestSerializer(data=request.data)

        if serializer.is_valid():

            result = create_booking(serializer.validated_data)

            return Response(
                {
                    "message": result[1],
                    "RequestID": result[0]
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PendingRequestsAPIView(APIView):

    def get(self, request):

        data = get_pending_requests()

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
