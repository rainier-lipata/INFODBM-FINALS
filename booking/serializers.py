from rest_framework import serializers


class BookingRequestSerializer(serializers.Serializer):

    StudentID = serializers.IntegerField()

    MentorID = serializers.IntegerField()

    AvailabilityID = serializers.IntegerField()

    TopicID = serializers.IntegerField()

    Message = serializers.CharField(max_length=500)