from django.db import models

from accounts.models import Profile


class Workout(models.Model):
    class Meta:
        db_table = "workouts"
        ordering = ["-date"]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
