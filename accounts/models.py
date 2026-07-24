from django.db import models


class User(models.Model):

    UserID = models.AutoField(primary_key=True)

    Email = models.EmailField(max_length=100, unique=True)

    PasswordHash = models.CharField(max_length=255)

    FirstName = models.CharField(max_length=50)

    LastName = models.CharField(max_length=50)

    Role = models.CharField(max_length=20)

    CreatedAt = models.DateTimeField()

    class Meta:
        db_table = 'Users'
        managed = False

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"