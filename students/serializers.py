from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()
    UserID = serializers.IntegerField()
    Course = serializers.CharField()
    YearLevel = serializers.IntegerField()


class StudentProfileSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()
    FirstName = serializers.CharField()
    LastName = serializers.CharField()
    Email = serializers.EmailField()
    Course = serializers.CharField()
    YearLevel = serializers.IntegerField()


class StudentDashboardSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()
    FirstName = serializers.CharField()
    LastName = serializers.CharField()
    UpcomingSessions = serializers.IntegerField()

