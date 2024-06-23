import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True)


class Club(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)


class Assignor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clubs = models.ManyToManyField(Club, through="AssignorClub")


class AssignorClub(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    assignor = models.ForeignKey(Assignor, on_delete=models.CASCADE)
    admin = models.BooleanField()


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assignor = models.ForeignKey(Assignor, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    home_team = models.CharField(max_length=128)
    away_team = models.CharField(max_length=128)
    date_time = models.DateTimeField()
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)
    location = models.CharField(max_length=128)
    league = models.CharField(max_length=128, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Referee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    applications = models.ManyToManyField(
        Job, through="Application", related_name="applied"
    )
    assignments = models.ManyToManyField(
        Job, through="Assignment", related_name="assigned"
    )
    clubs = models.ManyToManyField(Club)


class Assignment(models.Model):
    POSITIONS = {
        "C": "Center Referee",
        "AR": "Assistant Referee",
        "FAR": "Fourth Official",
        "VAR": "Video Assistant Referee",
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=3, choices=POSITIONS)
    referee = models.ForeignKey(
        Referee, on_delete=models.CASCADE, blank=True, null=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
