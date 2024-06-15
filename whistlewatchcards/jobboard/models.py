from django.db import models


class Job(models.Model):
    home_team = models.TextField()
    away_team = models.TextField()
    date_time = models.DateTimeField()
    location = models.TextField()
    league = models.TextField()
    club = models.TextField()

    def __str__(self):
        return self.name
