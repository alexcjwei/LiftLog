from django.shortcuts import render
from django.views import generic
from accounts import models


def get_profile(request):
    profile = models.Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})
