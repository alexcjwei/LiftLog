from django.urls import path

from . import views

app_name = "exercises"
urlpatterns = [
    path("", views.ExerciseListView.as_view(), name="index"),
    path("<int:pk>/", views.ExerciseDetailView.as_view(), name="detail"),
]
