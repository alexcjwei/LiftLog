from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from workouts import models
from workouts import forms


class WorkoutListView(LoginRequiredMixin, generic.ListView):
    model = models.Workout

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(profile=self.request.user.profile)
        return qs


class WorkoutDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Workout

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(profile=self.request.user.profile)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_exercise_form"] = forms.WorkoutExerciseForm()
        return context


class WorkoutUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Workout
    form_class = forms.WorkoutForm
    template_name_suffix = "_update_form"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(profile=self.request.user.profile)
        return qs

    def get_success_url(self):
        return reverse_lazy("workouts:detail", kwargs={"pk": self.object.id})


class WorkoutCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Workout
    form_class = forms.WorkoutForm
    success_url = reverse_lazy(
        "workouts:index"
    )  # A. Wei - Use reverse_lazy so there's no circular import.

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


@login_required
@require_POST
def workout_delete(request, pk):
    workout = get_object_or_404(models.Workout, pk=pk)
    if workout.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this workout.")
    workout.delete()
    return redirect("workouts:index")


@login_required
@require_POST
def workout_copy(request, pk):
    workout = get_object_or_404(models.Workout, pk=pk)
    if workout.user != request.user:
        # TODO maybe in the future, we can allow users to copy other users' workouts
        return HttpResponseForbidden("You are not allowed to copy this workout.")

    # Shallow copy the workout
    new_workout = workout
    new_workout.pk = None
    new_workout.name = f"{workout.name} (copy)"
    new_workout.date = date.today()
    new_workout.save()

    # Copy exercises
    exercises = models.WorkoutExercise.objects.filter(workout_id=pk)
    for workout_exercise in exercises:
        original_workout_exercise_id = workout_exercise.id
        new_workout_exercise = workout_exercise
        new_workout_exercise.pk = None
        # Relate the new workout to the new exercise
        new_workout_exercise.workout = new_workout
        new_workout_exercise.save()

        # Copy sets
        sets = models.Set.objects.filter(
            workout_exercise_id=original_workout_exercise_id
        )
        for set_ in sets:
            set_.pk = None
            set_.workout_exercise = new_workout_exercise
            set_.save()

    return redirect("workouts:index")


class WorkoutExerciseDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.WorkoutExercise

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(workout__profile=self.request.user.profile)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = context["workoutexercise"].workout
        context["add_set_form"] = forms.SetForm()
        return context


class WorkoutExerciseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.WorkoutExercise
    fields = ["exercise"]
    template_name_suffix = "_update_form"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(workout__profile=self.request.user.profile)
        return qs

    def get_success_url(self):
        return reverse_lazy(
            "workouts:workout_exercise_detail",
            kwargs={"pk": self.object.id},
        )


@login_required
@require_POST
def workout_exercise_add(request, workout_id):
    workout = get_object_or_404(models.Workout, pk=workout_id)
    if workout.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to add an exercise to this workout."
        )
    if request.method == "POST":
        form = forms.WorkoutExerciseForm(request.POST)
        if form.is_valid():
            workout_exercise = form.save(commit=False)
            workout_exercise.workout_id = workout_id
            workout_exercise.save()
            return redirect("workouts:detail", pk=workout_id)


@login_required
@require_POST
def workout_exercise_delete(request, workout_exercise_id):
    workout_exercise = get_object_or_404(models.WorkoutExercise, pk=workout_exercise_id)
    if workout_exercise.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this exercise.")
    workout_exercise.delete()
    return redirect("workouts:detail", pk=workout_exercise.workout_id)


@login_required
@require_POST
def workout_exercise_shift_order(request, workout_exercise_id, direction):
    workout_exercise = get_object_or_404(models.WorkoutExercise, pk=workout_exercise_id)
    if workout_exercise.user != request.user:
        return HttpResponseForbidden("You are not allowed to shift this exercise.")
    if direction == "up":
        workout_exercise.shift_order_up()
    elif direction == "down":
        workout_exercise.shift_order_down()
    return redirect("workouts:detail", pk=workout_exercise.workout_id)


@login_required
@require_POST
def set_add(request, workout_exercise_id):
    workout_exercise = get_object_or_404(models.WorkoutExercise, pk=workout_exercise_id)
    if workout_exercise.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to add a set to this exercise."
        )
    if request.method == "POST":
        form = forms.SetForm(request.POST)
        if form.is_valid():
            num_sets = form.cleaned_data["sets"]
            set_ = form.save(commit=False)
            set_.workout_exercise_id = workout_exercise_id
            sets = [set_] * num_sets
            models.Set.objects.bulk_create(sets)
            return redirect("workouts:workout_exercise_detail", pk=workout_exercise_id)


@login_required
@require_POST
def set_delete(request, pk):
    set_ = get_object_or_404(models.Set, pk=pk)
    if set_.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to add a set to this exercise."
        )
    set_.delete()
    return redirect("workouts:workout_exercise_detail", pk=set_.workout_exercise_id)


@login_required
@require_POST
def set_copy(request, pk):
    set_ = get_object_or_404(models.Set, pk=pk)
    if set_.user != request.user:
        return HttpResponseForbidden("You are not allowed to copy this set.")
    # A. Wei - By setting the pk to None, Django will create a new instance and autogen a new pk.
    set_.pk = None
    set_.save()
    return redirect("workouts:workout_exercise_detail", pk=set_.workout_exercise_id)


class SetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Set
    fields = ["weight", "weight_unit", "repetitions", "seconds"]
    template_name_suffix = "_update_form"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(workout_exercise__workout__profile=self.request.user.profile)
        return qs

    def get_success_url(self):
        return reverse_lazy(
            "workouts:workout_exercise_detail",
            kwargs={"pk": self.object.workout_exercise.id},
        )
