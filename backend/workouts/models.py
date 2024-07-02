from django.db import models
from django.urls import reverse

from accounts.models import Profile
from exercises.models import Exercise

from datetime import date


class Workout(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "workouts"
        ordering = ["-date", "-updated_at"]

    def __str__(self):
        return f"{self.name} - {self.date}"

    @property
    def user(self):
        return self.profile.user

    def can_user_manage(self, user):
        return self.user == user


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="exercises"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "workout_exercises"
        ordering = ["order"]

    def __str__(self):
        return f"{self.exercise.name} x {self.sets.count()} sets"

    @property
    def user(self):
        return self.workout.profile.user

    @property
    def average_weight(self):
        sets = self.sets.filter(weight__isnull=False)
        if sets:
            return sets.aggregate(models.Avg("weight"))["weight__avg"]

    @property
    def average_repetitions(self):
        sets = self.sets.filter(repetitions__isnull=False)
        if sets:
            return sets.aggregate(models.Avg("repetitions"))["repetitions__avg"]

    @property
    def average_seconds(self):
        sets = self.sets.filter(seconds__isnull=False)
        if sets:
            return sets.aggregate(models.Avg("seconds"))["seconds__avg"]

    def can_user_manage(self, user):
        return self.user == user

    def save(self, *args, **kwargs):
        # A. Wei - Newly saving exercises do not have a pk. Use this to add new exercises to the end of the list.
        if not self.pk:
            self.order = self.workout.exercises.count() + 1
        super().save(*args, **kwargs)

    def swap_order(self, other):
        self.order, other.order = other.order, self.order
        self.save()
        other.save()

    def shift_order_up(self):
        previous = self.workout.exercises.filter(order__lt=self.order).last()
        if previous:
            self.swap_order(previous)

    def shift_order_down(self):
        next_ = self.workout.exercises.filter(order__gt=self.order).first()
        if next_:
            self.swap_order(next_)


class Set(models.Model):
    workout_exercise = models.ForeignKey(
        WorkoutExercise, on_delete=models.CASCADE, related_name="sets"
    )
    weight = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    weight_unit = models.CharField(
        max_length=2, default="lb", choices=[("kg", "kgs"), ("lb", "lbs")]
    )
    repetitions = models.PositiveSmallIntegerField(null=True, blank=True)
    seconds = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = "sets"

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
