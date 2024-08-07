from django.urls import path, include
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("", views.ProfileListView.as_view(), name="index"),
    path("", include("django.contrib.auth.urls")),
    path("profile/", views.get_profile, name="profile"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
    path("follow/<int:pk>/", views.follow, name="follow"),
    path("unfollow/<int:pk>/", views.unfollow, name="unfollow"),
]
