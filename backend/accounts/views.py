from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from accounts import models


@login_required
def get_profile(request):
    profile = models.Profile.objects.get(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})
