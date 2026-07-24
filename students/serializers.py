from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentProfileSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()

    UserID = serializers.IntegerField()

    Course = serializers.CharField()

    YearLevel = serializers.IntegerField()

class StudentDashboardSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()

