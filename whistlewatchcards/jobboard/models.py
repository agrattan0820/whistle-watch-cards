from django.db import models
from django.contrib.auth.models import User

class Referee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PhoneNumberField()

class Assignor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PhoneNumberField()

class Job(models.Model):
    home_team = models.TextField()
    away_team = models.TextField()
    date_time = models.DateTimeField()
    location = models.TextField()
    league = models.TextField()
    club = models.TextField()

    def __str__(self):
        return self.name
