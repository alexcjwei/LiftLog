from django.urls import path

from . import views

app_name = "workouts"
urlpatterns = [
    path("", views.WorkoutListView.as_view(), name="index"),
    path("create/", views.WorkoutCreateView.as_view(), name="create"),
    path("<int:pk>/", views.WorkoutDetailView.as_view(), name="detail"),
    path(
        "<int:workout_id>/exercises/add/",
        views.workout_exercise_add,
        name="workout_exercise_add",
    ),
    path(
        "<int:workout_id>/exercises/<int:workout_exercise_id>/delete/",
        views.workout_exercise_delete,
        name="workout_exercise_delete",
    ),
    path(
        "<int:workout_id>/exercises/<int:pk>/",
        views.WorkoutExerciseDetailView.as_view(),
        name="workout_exercise_detail",
    ),
]
