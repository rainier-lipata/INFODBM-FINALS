from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'UserID',
            'Email',
            'FirstName',
            'LastName',
            'Role',
            'CreatedAt'
        ]

class RegisterStudentSerializer(serializers.Serializer):

    Email = serializers.EmailField()

    PasswordHash = serializers.CharField()

    FirstName = serializers.CharField(max_length=50)

    LastName = serializers.CharField(max_length=50)

    Course = serializers.CharField(max_length=100)

    YearLevel = serializers.IntegerField()

class RegisterMentorSerializer(serializers.Serializer):

    Email = serializers.EmailField()

    PasswordHash = serializers.CharField()

    FirstName = serializers.CharField(max_length=50)

    LastName = serializers.CharField(max_length=50)

    Bio = serializers.CharField()

    SkillLevel = serializers.CharField(max_length=20)

    YearsExperience = serializers.IntegerField()

class LoginSerializer(serializers.Serializer):
    Email = serializers.EmailField()

    PasswordHash = serializers.CharField(
        write_only=True
    )


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Email'
        ]

