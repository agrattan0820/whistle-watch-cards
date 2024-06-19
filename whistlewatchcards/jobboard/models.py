from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True)


class Club(models.Model):
    name = models.TextField()


class Assignor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clubs = models.ManyToManyField(Club, through="AssignorClub")


class AssignorClub(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    assignor = models.ForeignKey(Assignor, on_delete=models.CASCADE)
    admin = models.BooleanField()


class Job(models.Model):
    assignor = models.ForeignKey(Assignor, on_delete=models.CASCADE)
    home_team = models.TextField()
    away_team = models.TextField()
    date_time = models.DateTimeField()
    location = models.TextField()
    league = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Referee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    applications = models.ManyToManyField(Job, through="Application")
    assignments = models.ManyToManyField(Job, through="Assignment")
    clubs = models.ManyToManyField(Club)


class Assignment(models.Model):
    POSITIONS = {
        "C": "Center Referee",
        "AR": "Assistant Referee",
        "FAR": "Fourth Official",
        "VAR": "Video Assistant Referee",
    }

    position = models.CharField(max_length=3, choices=POSITIONS)
    referee = models.ForeignKey(
        Referee, on_delete=models.CASCADE, blank=True, null=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class Application(models.Model):
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
