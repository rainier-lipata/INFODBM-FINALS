from django.db import models

# Create your models here.

class BookingRequest(models.Model):

    RequestID = models.AutoField(primary_key=True)
    StudentID = models.IntegerField()
    MentorID = models.IntegerField()
    AvailabilityID = models.IntegerField()
    TopicID = models.IntegerField()
    Message = models.CharField(max_length=500)
    Status = models.CharField(max_length=20)
    RequestedAt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "BookingRequests"
