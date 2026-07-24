from django.db import models

# Create your models here.
class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    UserID = models.IntegerField()
    Course = models.CharField(max_length=100)
    YearLevel = models.IntegerField()

    class Meta:
        managed = False
        db_table = "Students"