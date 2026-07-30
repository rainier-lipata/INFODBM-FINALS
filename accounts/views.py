from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import (
    RegisterStudentSerializer,
    RegisterMentorSerializer,
    LoginSerializer,
    UpdateUserSerializer,
)

from .services import (
    create_student,
    create_mentor,
    login_user,
    update_user
)



class RegisterStudentAPIView(APIView):

    def post(self, request):

        serializer = RegisterStudentSerializer(data=request.data)

        if serializer.is_valid():

            create_student(serializer.validated_data)

            return Response(
                {
                    "message": "Student registered successfully."
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class RegisterMentorAPIView(APIView):

    def post(self, request):

        serializer = RegisterMentorSerializer(data=request.data)

        if serializer.is_valid():

            create_mentor(serializer.validated_data)

            return Response(
                {"message": "Mentor registered successfully."},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginAPIView(APIView):
        def post(self, request):

            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid():

                user = login_user(
                    serializer.validated_data["Email"],
                    serializer.validated_data["PasswordHash"]
                )

                if user:
                    return Response(
                        {
                            "message": "Login successful.",
                            "user": {
                                    "UserID": user[0],
                                    "StudentID": user[1],
                                    "MentorID": user[2],
                                    "FirstName": user[3],
                                    "LastName": user[4],
                                    "Role": user[5]
                            }
                        }
                    )

                return Response(
                    {
                        "message": "Invalid email or password."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class UpdateProfileAPIView(APIView):
        def put(self, request, user_id):
            serializer = UpdateUserSerializer(data=request.data)

            if serializer.is_valid():
                data = serializer.validated_data
                data["UserID"] = user_id

                update_user(data)

                return Response(
                    {
                        "message": "Profile updated successfully."
                    }
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )