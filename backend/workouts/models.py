from django.db import models
from django.urls import reverse

from accounts.models import Profile
from exercises.models import Exercise

from datetime import date


class Workout(models.Model):
    class Meta:
        db_table = "workouts"
        ordering = ["-date", "-updated_at"]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

    @property
    def user(self):
        return self.profile.user

    def can_user_manage(self, user):
        return self.user == user


class WorkoutExercise(models.Model):
    class Meta:
        db_table = "workout_exercises"

    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="exercises"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exercise.name} x {self.sets.count()} sets"

    @property
    def user(self):
        return self.workout.profile.user

    def can_user_manage(self, user):
        return self.user == user


class Set(models.Model):
    class Meta:
        db_table = "sets"

    workout_exercise = models.ForeignKey(
        WorkoutExercise, on_delete=models.CASCADE, related_name="sets"
    )
    weight = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    weight_unit = models.CharField(
        max_length=2, default="lb", choices=[("kg", "kgs"), ("lb", "lbs")]
    )
    repetitions = models.PositiveSmallIntegerField(null=True, blank=True)
    seconds = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        components = []
        if self.weight:
            weight = f"{self.weight}".rstrip("0").rstrip(".")
            components.append(f"{weight} {self.weight_unit}s")
        if self.repetitions:
            components.append(f"{self.repetitions} reps")
        if self.seconds:
            components.append(f"{self.seconds} sec")

        return " - ".join(components)

    @property
    def user(self):
        return self.workout_exercise.workout.profile.user

    def can_user_manage(self, user):
        return self.user == user
