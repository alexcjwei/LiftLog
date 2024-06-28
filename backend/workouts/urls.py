from django.urls import path

from . import views

app_name = "workouts"

workout_patterns = [
    path("", views.WorkoutListView.as_view(), name="index"),
    path("create/", views.WorkoutCreateView.as_view(), name="create"),
    path("<int:pk>/", views.WorkoutDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.WorkoutUpdateView.as_view(), name="update"),
    path("<int:pk>/copy", views.workout_copy, name="copy"),
    path("<int:pk>/delete", views.workout_delete, name="delete"),
]
workout_exercise_patterns = [
    path(
        "<int:workout_id>/add-exercise/",
        views.workout_exercise_add,
        name="workout_exercise_add",
    ),
    path(
        "exercises/<int:workout_exercise_id>/delete/",
        views.workout_exercise_delete,
        name="workout_exercise_delete",
    ),
    path(
        "exercises/<int:pk>/",
        views.WorkoutExerciseDetailView.as_view(),
        name="workout_exercise_detail",
    ),
]
set_patterns = [
    path("", views.WorkoutListView.as_view(), name="index"),
    path("create/", views.WorkoutCreateView.as_view(), name="create"),
    path("<int:pk>/", views.WorkoutDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.WorkoutUpdateView.as_view(), name="update"),
    path("<int:pk>/copy", views.workout_copy, name="copy"),
    path("<int:pk>/delete", views.workout_delete, name="delete"),
]

urlpatterns = workout_patterns + workout_exercise_patterns + set_patterns
