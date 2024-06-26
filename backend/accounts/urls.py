from django.urls import path, include
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("profile/", views.get_profile, name="profile"),
]
