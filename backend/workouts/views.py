from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
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


class WorkoutCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Workout
    form_class = forms.WorkoutForm
    success_url = reverse_lazy(
        "workouts:index"
    )  # A. Wei - Use reverse_lazy so there's no circular import.

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
