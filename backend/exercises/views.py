from django.shortcuts import render, get_object_or_404
from django.views import generic
from exercises.models import Exercise
from typing import Any, Dict, List
from workouts.models import WorkoutExercise


class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = "exercises/index.html"


class ExerciseDetailView(generic.DetailView):
    model = Exercise

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["exercise_history"] = self._get_exercise_history()
        return context

    def _get_exercise_history(self) -> Dict[str, List]:
        """
        Returns a dictionary with labels and data for the exercise history chart,
        like {"labels": ["2021-01-01", "2021-01-02"], "data": [100, 105]}

        TODO add detail on hover (reps, sets)
        TODO average weights on same training day
        """
        exercise_history = {"labels": [], "data": []}
        exercises = WorkoutExercise.objects.filter(
            exercise=self.object,
            workout__profile=self.request.user.profile,
        ).order_by("workout__date")

        for exercise in exercises:
            exercise_history["labels"].append(str(exercise.workout.date))
            exercise_history["data"].append(float(exercise.average_weight))

        return exercise_history
