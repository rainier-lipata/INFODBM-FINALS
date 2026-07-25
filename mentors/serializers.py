from rest_framework import serializers

class AvailabilitySerializer(serializers.Serializer):

    AvailableDate = serializers.DateField()
    StartTime = serializers.TimeField()
    EndTime = serializers.TimeField()

class MentorExpertiseSerializer(serializers.Serializer):

    MentorID = serializers.IntegerField()

    TopicID = serializers.IntegerField()