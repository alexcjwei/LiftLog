from django.urls import path

from . import views

app_name = "workouts"
urlpatterns = [
    path("", views.WorkoutListView.as_view(), name="index"),
    path("<int:pk>/", views.WorkoutDetailView.as_view(), name="detail"),
    path("create/", views.WorkoutCreateView.as_view(), name="create"),
]
