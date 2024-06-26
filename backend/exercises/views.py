from django.shortcuts import render, get_object_or_404
from django.views import generic
from exercises.models import Exercise


class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = "exercises/index.html"


class ExerciseDetailView(generic.DetailView):
    model = Exercise
