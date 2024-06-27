from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_exercise_form"] = forms.WorkoutExerciseForm()
        return context


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
def workout_delete(request, pk):
    workout = get_object_or_404(models.Workout, pk=pk)
    workout.delete()
    return redirect("workouts:index")


@login_required
def workout_copy(request, pk):
    workout = get_object_or_404(models.Workout, pk=pk)
    workout.pk = None
    workout.save()
    return redirect("workouts:index")


class WorkoutExerciseDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.WorkoutExercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = context["workoutexercise"].workout
        context["add_set_form"] = forms.SetForm()
        return context


@login_required
def workout_exercise_add(request, workout_id):
    if request.method == "POST":
        form = forms.WorkoutExerciseForm(request.POST)
        if form.is_valid():
            workout_exercise = form.save(commit=False)
            workout_exercise.workout_id = workout_id
            workout_exercise.save()
            return redirect("workouts:detail", pk=workout_id)


@login_required
def workout_exercise_delete(request, workout_exercise_id):
    workout_exercise = get_object_or_404(models.WorkoutExercise, pk=workout_exercise_id)
    workout_exercise.delete()
    return redirect("workouts:detail", pk=workout_id)


@login_required
def set_add(request, workout_exercise_id):
    workout_exercise = get_object_or_404(models.WorkoutExercise, pk=workout_exercise_id)
    if request.method == "POST":
        form = forms.SetForm(request.POST)
        if form.is_valid():
            set = form.save(commit=False)
            set.workout_exercise_id = workout_exercise_id
            set.save()
            return redirect("workouts:workout_exercise_detail", pk=workout_exercise_id)


@login_required
def set_delete(request, pk):
    set = get_object_or_404(models.Set, pk=pk)
    set.delete()
    return redirect("workouts:workout_exercise_detail", pk=set.workout_exercise_id)


@login_required
def set_copy(request, pk):
    set = get_object_or_404(models.Set, pk=pk)
    # A. Wei - By setting the pk to None, Django will create a new instance and autogen a new pk.
    set.pk = None
    set.save()
    return redirect("workouts:workout_exercise_detail", pk=set.workout_exercise_id)


class SetDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Set


class SetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Set
    fields = ["weight", "weight_unit", "repetitions", "seconds"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy(
            "workouts:workout_exercise_detail",
            kwargs={"pk": self.object.workout_exercise.id},
        )
